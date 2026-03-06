from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from cafein_api.core.supabase import supabase

class ManualItem(BaseModel):
    id: int           # 스크린샷에 int8로 되어 있으니 int로 변경
    item_name: str    # item_name으로 변경
    price: int        # price 컬럼 추가
    recipe: Optional[str] = None      # 추가: DB에서 가져올 레시피
    equipment: Optional[str] = None   # 추가: DB에서 가져올 장비 가이드
    
    class Config:
        from_attributes = True