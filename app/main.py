import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
async def read_root():
    return({'message': 'Root endpoint'})

@app.get("/health")
async def check_health():
    return {'status': 'ok'}
