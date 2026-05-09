from fastapi import FastAPI
from api.routes import workflows
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev mode
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# include all routes
app.include_router(workflows.router)


# ------------------------
# HEALTH CHECK
# ------------------------
@app.get("/")
def home():
    return {"message": "AI Multi-Agent System is running 🚀"}