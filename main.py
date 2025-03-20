from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


#allow frontend to fetch data from the  backend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # need to change this to my domian once in prod
    allow_credintals=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

# sample court data
pickleball_courts = [
    {"lat": 37.7749, "lng": -122.4194},  # San Francisco
    {"lat": 34.0522, "lng": -118.2437},  # Los Angeles
]
# define request model
class Court(BaseModel):
    lat: float
    lng: float

@app.get("/api/courts")
def get_courts():
    return pickleball_courts

@app.post("/api/add_court")
def add_court(court:Court):
    pickleball_courts.append({"lat":court.lat, "lng":court.lng})
    return{"message": "Court was successfully added!", "lat":court.lat, "lng": court.lng}
