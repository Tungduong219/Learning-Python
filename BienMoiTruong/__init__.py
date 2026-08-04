import os

# 1. Lấy tên Hệ điều hành đang chạy (posix = Linux/macOS, nt = Windows)
print("Hệ điều hành hiện tại:", os.name)

# 2. Giả lập việc tạo một "Ghi chú" (Biến môi trường) mới trên hệ thống
os.environ["APP_MODE"] = "Development"

# 3. Trích xuất giá trị vừa đặt ra màn hình
current_mode = os.environ.get("APP_MODE")
print(f"Ứng dụng đang chạy ở chế độ: {current_mode}")


import json

# 1. Khai báo một Dictionary chứa cấu hình ứng dụng
config_data = {
    "app_name": "MyPythonApp",
    "version": "1.0.0",
    "security": {
        "api_key_status": "Loaded",
        "masked_key": "AIzaSy...9876"  # Đã mask để bảo mật
    }
}

# 2. Đóng gói Dictionary thành Chuỗi JSON (Pretty Print)
json_string = json.dumps(
    config_data,
    indent=4,            # Thụt lề 4 khoảng trắng cho dễ đọc
    ensure_ascii=False   # Giữ nguyên tiếng Việt/ký tự đặc biệt
)

print("--- CHUỖI JSON SAU CHI ĐÓNG GÓI ---")
print(json_string)
print(f"Kiểu dữ liệu: {type(json_string)}")