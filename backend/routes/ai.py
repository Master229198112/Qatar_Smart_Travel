from fastapi import APIRouter
from db.mongo import db

router = APIRouter()

@router.get("/suggest")
def ai_reallocation():
    # Sample rule logic
    t1 = db.queue_entries.count_documents({"type": "T1"})
    t2 = db.queue_entries.count_documents({"type": "T2"})
    t3 = db.queue_entries.count_documents({"type": "T3"})

    if t1 > 10:
        return {"suggestion": "Divert 2 counters from T3 to T1 to ease assisted passenger queue."}
    elif t2 > 10:
        return {"suggestion": "Shift one T3 counter to handle business class temporarily."}
    else:
        return {"suggestion": "Queues are balanced. Maintain FIFO for T3."}
