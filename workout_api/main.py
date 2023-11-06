from fastapi import FastAPI
from workout_api.routers import api_router
import uvicorn

app = FastAPI(title='WorkoutAPI')
app.include_router(api_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('mains:app', host='0.0.0.0', port=8000, log_level='info', reload=True)