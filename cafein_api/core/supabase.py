import os
from dotenv import load_dotenv
from supabase import create_client, Client

# .env 파일의 절대 경로를 직접 지정합니다.
# 용성님의 새로운 폴더 경로에 맞췄습니다.
env_path = r"C:\workspace\intel_2026\cafein\.env"
load_dotenv(dotenv_path=env_path)

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

# 데이터가 잘 들어왔는지 터미널에 찍어봅니다. (서버 켜질 때 확인용)
if not url or not key:
    print(f"--- 설정 오류 발생 ---")
    print(f"찾으려는 .env 경로: {env_path}")
    raise ValueError("앗! .env 파일에서 정보를 불러오지 못했습니다.")

supabase: Client = create_client(url, key)