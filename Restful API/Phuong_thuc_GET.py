import requests
url = "https://jsonplaceholder.typicode.com/posts"
params = {
    "userId":1
}

#Gửi GET request
response = requests.get(url,params=params)

#Kiểm tra Status Code (200 OK nghĩa là thành công)
print("Status code: ", response.status_code)

#Chuyển dữ liệu Json nhận được thành kiểu dữ liệu Python (List/Dict)
data = response.json()
print(f"Lấy được {len(data)} của user 1")
print("Bài viết đầu tiên: ",data[0]["title"])


#Phương thức POST
new_post = {
    "title": "Học REST API với Python",
    "body" : "Nội dung bài học về phương thức POST",
    "userId":1
}
response = requests.post(url,json=new_post)
print("Status code: ", response.status_code)
print("Dữ liệu phản hồi sau khi tạo: ",response.json())


#Định nghĩa với Headers
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "MyPythonApp/1.0",
    "Authorization": "Bearer my_secret_token_123"
}

data = {
    "title": "Test Header",
    "body":"Gửi request kèm Header",
    "userId":1
}

response = requests.post(url,json=data, headers=headers)
print(response.json())
print("Status code: ", response.status_code)