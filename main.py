from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

def create_app():
    app = FastAPI()

    from src.supa.client import sb
    from src.middlewares.auth import CustomAuthMiddleware

    # Import and register the API endpoints
    from src.routes.events import events_router
    from src.routes.auth import auth_router
    from src.routes.users import users_router
    from src.routes.bookings import bookings_router
    from src.routes.devices import devices_router
    from src.routes.access import access_router

    # Add middleware
    app.add_middleware(CustomAuthMiddleware, supabase=sb)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Add the routers
    app.include_router(auth_router, prefix="/auth", tags=["auth"])
    app.include_router(users_router, prefix="/users", tags=["users"])
    app.include_router(events_router, prefix="/events", tags=["events"])
    app.include_router(bookings_router, prefix="/bookings", tags=["bookings"])
    app.include_router(devices_router, prefix="/devices", tags=["devices"])
    app.include_router(access_router, prefix="/access", tags=["access"])

    # Health check
    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)