# C:\workspace\intel_2026\cafein\cafein_api\routers\manual.py
from fastapi import APIRouter, HTTPException
from typing import List
# 앞에 cafein_api. 을 붙여서 경로를 확실히 합니다.
from cafein_api.core.supabase import supabase
from cafein_api.models.manual import ManualItem

router = APIRouter(prefix="/api/manual", tags=["Manual"])

@router.get("/list", response_model=List[ManualItem])
async def get_all_manuals():
    result = supabase.table("menu").select("*").execute()
    return result.data

@router.get("/{manual_id}", response_model=ManualItem)
async def get_manual_detail(manual_id: str):
    result = supabase.table("menu").select("*").eq("id", manual_id).single().execute()
    if not result.data:
        raise HTTPException(status_code=404, detail="매뉴얼을 찾을 수 없습니다.")
    return result.data