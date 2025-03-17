from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
#allow frontend to fetch data from fastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credintals=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

# sample court data
pickleball_courts = [
    {"lat": 37.7749, "lng": -122.4194},  # San Francisco
    {"lat": 34.0522, "lng": -118.2437},  # Los Angeles
    {"lat": 40.7128, "lng": -74.0060},   # New York
]

@app.get("/api/courts")
def get_courts():
    return pickleball_courts