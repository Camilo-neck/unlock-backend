from fastapi import FastAPI
import uvicorn

def create_app():
    app = FastAPI()

    from src.supa.client import sb
    from src.middlewares.auth import CustomAuthMiddleware

    # Import and register the API endpoints
    from src.routes.events import events_router
    from src.routes.auth import auth_router
    from src.routes.users import users_router

    # Add middleware
    app.add_middleware(CustomAuthMiddleware, supabase=sb)

    # Add the routers
    app.include_router(auth_router, prefix="/auth")
    app.include_router(users_router, prefix="/users")
    app.include_router(events_router, prefix="/events")

    # Health check
    @app.get("/health")
    async def health():
        return {"status": "ok"}

    return app

app = create_app()

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)