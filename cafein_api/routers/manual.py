# C:\workspace\intel_2026\cafein\cafein_api\routers\manual.py
from fastapi import APIRouter, HTTPException
from typing import List
# 앞에 cafein_api. 을 붙여서 경로를 확실히 합니다.
from cafein_api.core.supabase import supabase
from cafein_api.models.manual import ManualItem

router = APIRouter(prefix="/api/manual", tags=["Manual"])

# 메뉴 리스트 조회
@router.get("/list") 
async def get_all_manuals():
    result = supabase.table("menu").select("*").execute()
    return result.data

# FAQ(긴급 상황) 리스트 조회 (새로 추가)
@router.get("/faq") # 최종 주소: /api/manual/faq
async def get_faq_list():
    result = supabase.table("faqs").select("*").order("is_important", desc=True).execute()
    return result.data

@router.get("/{manual_id}")  # 상세 조회용 엔드포인트
async def get_manual_detail(manual_id: int):
    # Supabase에서 id가 같은 녀석을 딱 하나(single) 가져옴
    result = supabase.table("menu").select("*").eq("id", manual_id).single().execute()
    return result.data

    
