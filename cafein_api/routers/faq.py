# C:\workspace\intel_2026\cafein\cafein_api\routers\faq.py
from fastapi import APIRouter, HTTPException
from cafein_api.core.supabase import supabase  # 수정
from cafein_api.routers.faq import FAQItem      # 수정
from typing import List

router = APIRouter(prefix="/api/faq", tags=["FAQ"])

# 1. FAQ 전체 목록 가져오기
@router.get("/list", response_model=List[FAQItem])
async def get_all_faqs():
    # 중요(is_important)한 항목이 위로 오도록 정렬해서 가져옵니다.
    result = supabase.table("faqs").select("*").order("is_important", desc=True).execute()
    return result.data

# 2. 특정 FAQ 상세 보기 (필요할 경우를 대비)
@router.get("/{faq_id}", response_model=FAQItem)
async def get_faq_detail(faq_id: int):
    result = supabase.table("faqs").select("*").eq("id", faq_id).single().execute()
    
    if not result.data:
        raise HTTPException(status_code=404, detail="해당 FAQ를 찾을 수 없습니다.")
    
    return result.data