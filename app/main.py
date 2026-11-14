import fastapi
from app import db

app = fastapi.FastAPI()

@app.get("/")
async def read_root():
    return { 'message' : 'Root endpoint' }

@app.get("/health")
async def check_health():
    return { 'status' : 'ok' }

@app.get("/ready")
def check_ready():
    if db.get_health_check():
        return { 'status' : 'ready' }
    else:
        return fastapi.responses.JSONResponse(status_code=503, content={ 'status' : 'unavailable' })
