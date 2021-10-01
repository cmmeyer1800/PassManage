from fastapi import FastAPI
from pydantic import BaseModel
import crypto

class Data(BaseModel):
    message: str

app = FastAPI()
encryption = crypto.encryption()