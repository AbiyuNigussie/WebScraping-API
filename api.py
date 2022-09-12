from typing import Union
from fastapi import FastAPI
from scraper import foods
app = FastAPI()

@app.get('/')
def home():
  return {"message": "Hello, This is Home Route!"}

@app.get("/api/foods")
def read_items():
  return {"foods": str(foods)}

@app.get("/api/foods/{food_id}")
def single_item(food_id):
  return {str(food_id): str(foods[int(food_id)])}