from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Union


from pymongo import MongoClient

app = FastAPI()


conn = MongoClient("mongodb://localhost:27017")




