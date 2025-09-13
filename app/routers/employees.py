
from fastapi import Depends
from app.auth import get_current_user
from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional
from app.db import employees_collection
from app.schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate
from app.models import doc_to_employee, date_to_datetime
from pymongo import ReturnDocument
from bson.objectid import ObjectId
from datetime import datetime

router = APIRouter(prefix="/employees", tags=["employees"])



@router.post("", response_model=EmployeeOut, status_code=status.HTTP_201_CREATED)
async def create_employee(emp: EmployeeCreate, current_user: dict = Depends(get_current_user)):
    
    existing = await employees_collection.find_one({"employee_id": emp.employee_id})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"employee_id '{emp.employee_id}' already exists."
        )

    doc = {
        "employee_id": emp.employee_id,
        "name": emp.name,
        "department": emp.department,
        "salary": emp.salary,
        
        "joining_date": date_to_datetime(emp.joining_date),
        "skills": emp.skills,
    }

    res = await employees_collection.insert_one(doc)
    created = await employees_collection.find_one({"_id": res.inserted_id})
    return doc_to_employee(created)


@router.get("/avg-salary")
async def avg_salary_by_department():
    pipeline = [
        {
            "$group": {
                "_id": "$department",
                "avg_salary": {"$avg": "$salary"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "department": "$_id",
                "avg_salary": {"$round": ["$avg_salary", 2]}
            }
        },
        {
            "$sort": {"department": 1}
        }
    ]
    cursor = employees_collection.aggregate(pipeline)
    result = []
    async for doc in cursor:
        result.append(doc)
    return result

@router.get("/search", response_model=List[EmployeeOut])
async def search_by_skill(skill: str = Query(..., description="Skill to search for")):
   
    cursor = employees_collection.find({"skills": {"$regex": f"^{skill}$", "$options": "i"}})
    docs = await cursor.to_list(length=1000)
    return [doc_to_employee(d) for d in docs]


@router.get("/{employee_id}", response_model=EmployeeOut)
async def get_employee(employee_id: str, current_user: dict = Depends(get_current_user)):
    doc = await employees_collection.find_one({"employee_id": employee_id})
    if not doc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return doc_to_employee(doc)

@router.put("/{employee_id}", response_model=EmployeeOut)
async def update_employee(employee_id: str, emp: EmployeeUpdate, current_user: dict = Depends(get_current_user)):
  
    update_fields = {}
    if emp.name is not None:
        update_fields["name"] = emp.name
    if emp.department is not None:
        update_fields["department"] = emp.department
    if emp.salary is not None:
        update_fields["salary"] = emp.salary
    if emp.joining_date is not None:
        update_fields["joining_date"] = date_to_datetime(emp.joining_date)
    if emp.skills is not None:
        update_fields["skills"] = emp.skills

    if not update_fields:
        
        doc = await employees_collection.find_one({"employee_id": employee_id})
        if not doc:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
        return doc_to_employee(doc)

    updated = await employees_collection.find_one_and_update(
        {"employee_id": employee_id},
        {"$set": update_fields},
        return_document=ReturnDocument.AFTER
    )

    if not updated:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return doc_to_employee(updated)

@router.delete("/{employee_id}")
async def delete_employee(employee_id: str, current_user: dict = Depends(get_current_user)):
    result = await employees_collection.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return {"status": "success", "message": f"Employee {employee_id} deleted."}

@router.get("", response_model=List[EmployeeOut])
async def list_employees(department: Optional[str] = Query(None, description="Filter by department")):
    query = {}
    if department:
        query["department"] = department
   
    cursor = employees_collection.find(query).sort("joining_date", -1)
    docs = await cursor.to_list(length=1000)
    return [doc_to_employee(d) for d in docs]