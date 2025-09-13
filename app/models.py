from datetime import datetime, time
from typing import Dict, Any

def doc_to_employee(doc: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert MongoDB document to API-friendly dict.
    """
    if not doc:
        return None
    return {
        "employee_id": doc.get("employee_id"),
        "name": doc.get("name"),
        "department": doc.get("department"),
        "salary": doc.get("salary"),
        "joining_date": doc.get("joining_date"),
        "skills": doc.get("skills", []),
    }

def date_to_datetime(d):
    """
    Convert a date (datetime.date) to a timezone-naive datetime at midnight for storage.
    """
    if d is None:
        return None
    if isinstance(d, datetime):
        return d
    return datetime.combine(d, time.min)