import fastapi, uvicorn

app = fastapi.FastAPI()

@app.get("/")
async def read_root():
    return({'message': 'Root endpoint'})

@app.get("/health")
async def check_health():
    return({'status': str(fastapi.status.HTTP_200_OK)})