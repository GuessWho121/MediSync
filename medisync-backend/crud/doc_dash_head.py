from sqlalchemy.orm import Session
import models
from typing import Optional

def get_doctor_dashboard_info(db: Session, userid: int) -> Optional[models.Doctor]:
    return db.query(models.Doctor)\
             .filter(models.Doctor.id == userid)\
             .first()

def format_dashboard_response(doctor: models.Doctor):
    """
    Format doctor data for dashboard display
    """
    return {
        "name": doctor.name,
        "doctor_id": f"D{doctor.id:05d}",  # Format: P00001, P00002, etc.
        "age": doctor.age,
        "blood_group": doctor.blood_group,
    }