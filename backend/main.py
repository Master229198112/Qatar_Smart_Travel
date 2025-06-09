from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.passenger import router as passenger_router
from routes.counter import router as counter_router
from routes.queue import router as queue_router
from routes.ai import router as ai_router
from routes.alerts import router as alerts_router
from routes.flight import router as flight_router
from routes.ws import router as ws_router
from routes.boardingpass import router as bp_router

app = FastAPI()

# CORS: allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route mounting
app.include_router(passenger_router, prefix="/api/passenger")
app.include_router(counter_router, prefix="/api/counter")
app.include_router(queue_router, prefix="/api/queue")
app.include_router(ai_router, prefix="/api/ai")
app.include_router(alerts_router, prefix="/api/alerts")
app.include_router(flight_router, prefix="/api/flights")
app.include_router(ws_router)
app.include_router(bp_router, prefix="/api/boarding")

@app.get("/")
def root():
    return {"message": "Qatar Smart Travel Backend is running"}
