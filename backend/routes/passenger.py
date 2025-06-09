from fastapi import APIRouter, Request
from db.mongo import db
from fastapi import HTTPException
from bson import ObjectId

router = APIRouter()

@router.post("/register")
async def register_passenger(request: Request):
    body = await request.json()
    result = db.passengers.insert_one(body)
    return {"message": "Passenger registered", "id": str(result.inserted_id)}

@router.get("/checkin/{passenger_id}")
async def checkin(passenger_id: str):
    passenger = db.passengers.find_one({"_id": ObjectId(passenger_id)})
    if not passenger:
        raise HTTPException(status_code=404, detail="Passenger not found")

    # Dummy logic: Assign terminal based on profile
    if passenger.get("special_needs"):
        terminal = "T1"
    elif passenger.get("class") == "Business" or passenger.get("passport") == "Qatari":
        terminal = "T2"
    else:
        terminal = "T3"

    return {
        "message": f"Passenger assigned to Terminal {terminal}",
        "name": passenger.get("name"),
        "terminal": terminal,
        "counter_number": "Counter-07",
        "eta": "3 min walk",
        "next_steps": "Proceed to security check after this"
    }
