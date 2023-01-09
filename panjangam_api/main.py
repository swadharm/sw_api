from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
#from fastapi.templating import Jinja2Templates
from typing import Union,Optional
from pytz import timezone
from pydantic import BaseModel

from sankalpam_live import *
from db import *
from city_info_update import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#temp = Jinja2Templates('html')

class City(BaseModel):
    name: str
    Latitude: str 
    Longitude: str
    time_zone: str

@app.get("/sankalpam_live/{city}/{languae}")
async def sankalpam_live(city,languae):
    a = sankalpam_all(city,languae)
    return  a

@app.post("/city_update/")
async def create_city(city: City):
    city_update(city.name,city.Latitude,city.Longitude,city.time_zone)
    return {'status':200}

@app.get("/time_zone_list")
async def time_zone_list():
    ans = []
    data = select_sql('*','time_zone')
    for i in data:
        ans.append(i[1])
    return  ans

@app.get("/city_list")
async def city_list():
    ans = []
    data = select_sql('*','city')
    for i in data:
        ans.append(i[1])
    return  ans