from fastapi import APIRouter
from db.mongo import db

router = APIRouter()

@router.get("/live-status")
def get_live_counters():
    counters = list(db.counters.find({}, {"_id": 0}))
    return {"counters": counters}

@router.get("/analytics")
def counter_analytics():
    counters = list(db.counters.find({}, {"_id": 0}))
    total = sum(c["waitTime"] for c in counters)
    passenger_distribution = {"T1": 0, "T2": 0, "T3": 0}

    for c in counters:
        passenger_distribution[c["type"]] += 1

    return {
        "totalCounters": len(counters),
        "avgWaitTime": round(total / len(counters), 2) if counters else 0,
        "distribution": passenger_distribution,
        "barChart": [{"counter": c["id"], "passengers": c["waitTime"] * 2} for c in counters]  # fake scale
    }
