import json
import os

def process_user_payload(raw_user_payload:str) -> dict:
    api_key = os.environ.get("API_KEY")
    if api_key is None:
        api_key = "DEMO_KEY_123456789."
    try:
        with open("raw_user_payload.json", "r",encoding="utf-8") as f:
            raw_user_payload = json.load(f)
            print("Doc File thanh cong")
    except FileNotFoundError:
        print("Khong tim thay tep")
    except json.JSONDecodeError:
        print("Tep bi loi dinh dang")



