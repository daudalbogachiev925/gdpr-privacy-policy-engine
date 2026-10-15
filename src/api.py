from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .engine import enforce_policy
from .models import Policy

app = FastAPI(title="GDPR Privacy Policy Engine")

class EnforceRequest(BaseModel):
    data: dict
    policy: Policy

class EnforceResponse(BaseModel):
    compliant: bool

@app.post("/enforce", response_model=EnforceResponse)
def enforce(request: EnforceRequest):
    try:
        compliant = enforce_policy(request.data, request.policy)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    return EnforceResponse(compliant=compliant)
