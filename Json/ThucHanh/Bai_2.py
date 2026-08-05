import json
products = [
    {"id": 1, "name": "Bàn phím cơ", "price": 1200000, "in_stock": True},
    {"id": 2, "name": "Chuột không dây", "price": 450000, "in_stock": False},
    {"id": 3, "name": "Màn hình 24 inch", "price": 3200000, "in_stock": True}
]
file_name = "store_data.json"
with open(file_name,"w",encoding="utf-8") as f:
    json.dump(products,f,ensure_ascii=False,indent=4,sort_keys=True)

print("-"*15+"Đọc lại file Json vừa tạo"+"-"*15)
with open(file_name,"r",encoding="utf-8") as f:
    store_data = json.load(f)
for item in store_data:
    if item["in_stock"]:
        print(item["name"])
