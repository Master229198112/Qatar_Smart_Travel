from fastapi import APIRouter, Request
from db.mongo import db
from datetime import datetime

router = APIRouter()

# Passenger raises help request
@router.post("/request-assist")
async def request_assistance(request: Request):
    data = await request.json()
    data["timestamp"] = datetime.utcnow()
    db.assistance_requests.insert_one(data)
    return {"message": "Assistance request logged."}

# Admin fetches active requests
@router.get("/live-requests")
def get_assistance_requests():
    requests = list(db.assistance_requests.find({}, {"_id": 0}).sort("timestamp", -1).limit(20))
    return {"requests": requests}

# Admin fetches alerts
@router.get("/emergency-alerts")
def get_system_alerts():
    alerts = list(db.system_alerts.find({}, {"_id": 0}).sort("timestamp", -1).limit(10))
    return {"alerts": alerts}
