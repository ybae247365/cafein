# C:\workspace\intel_2026\cafein\main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# 폴더 구조에 맞춰서 정확히 import
from cafein_api.routers import manual

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# manual 라우터만 등록
app.include_router(manual.router)


@app.get("/")
def root():
    return {"status": "success", "message": "Cafein FastAPI Server is Running!"}