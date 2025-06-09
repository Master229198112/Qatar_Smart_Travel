from fastapi import APIRouter, WebSocket
from db.mongo import db
import asyncio

router = APIRouter()

@router.websocket("/ws/counters")
async def websocket_counter_status(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            counters = list(db.counters.find({}, {"_id": 0}))
            await websocket.send_json({"counters": counters})
            await asyncio.sleep(5)  # Update every 5 seconds
    except Exception as e:
        print(f"[WebSocket] Disconnected: {e}")
