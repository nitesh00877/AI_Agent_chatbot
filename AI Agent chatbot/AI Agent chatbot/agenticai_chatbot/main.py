from fastapi import FastAPI
from app.route import router

app = FastAPI(title="LangGraph AI Agent")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    # Default to port 9999 to avoid local port conflicts; frontend can be updated to match.
    uvicorn.run("main:app", host="127.0.0.1", port=9999, reload=True)
