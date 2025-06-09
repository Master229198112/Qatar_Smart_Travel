from fastapi import APIRouter, Request
from db.mongo import db
from datetime import datetime

router = APIRouter()

@router.post("/new-entry")
async def new_queue_entry(request: Request):
    data = await request.json()
    data["timestamp"] = datetime.utcnow()
    result = db.queue_entries.insert_one(data)
    return {"message": "Queue entry added", "id": str(result.inserted_id)}
