from fastapi import APIRouter
from db.mongo import db
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/upcoming")
def get_flight_load():
    now = datetime.utcnow()
    next_2_hr = now + timedelta(hours=2)

    flights = list(db.flights.find(
        {"departureTime": {"$gte": now, "$lte": next_2_hr}},
        {"_id": 0}
    ))

    alerts = []
    for f in flights:
        if f.get("expectedPassengers", 0) > 250:
            alerts.append({
                "flight": f["flightNo"],
                "terminal": f["terminal"],
                "passengers": f["expectedPassengers"],
                "warning": "⚠️ Heavy load expected soon!"
            })

    return {
        "flights": flights,
        "alerts": alerts
    }
