from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Import and register the example API endpoints
from src.routes.users import users_router
from src.routes.events import events_router

app.include_router(users_router, prefix="/users")
app.include_router(events_router, prefix="/events")

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)