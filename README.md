# Learning Python 🐍

Tài liệu học tập và thực hành ngôn ngữ lập trình Python từ cơ bản đến nâng cao. Kho lưu trữ này chứa các ví dụ minh họa chi tiết về cú pháp, biến, kiểu dữ liệu và toán tử trong Python.

## 📂 Danh sách các bài học & Tệp nguồn

Dưới đây là chi tiết nội dung các tệp mã nguồn có trong kho lưu trữ này:

### 1. [Start.py](file:///d:/Workspace/University/Python/Start.py)
* **Nội dung:** Giới thiệu sơ lược và làm quen với Python.
* **Chi tiết:**
  * Khai báo biến và in dữ liệu cơ bản.
  * Cách kiểm tra kiểu dữ liệu với `type()`.
  * Các quy tắc đặt tên biến phổ biến (Camel Case, Pascal Case, Snake Case).
  * Gán giá trị cho nhiều biến và kỹ thuật Unpacking (giải nén list).
  * Phạm vi của biến (biến toàn cục - Global Variables).

### 2. [CuPhapCoBan.py](file:///d:/Workspace/University/Python/CuPhapCoBan.py)
* **Nội dung:** Tìm hiểu về các quy tắc cú pháp cốt lõi của Python.
* **Chi tiết:**
  * Tầm quan trọng của thụt đầu dòng (Indentation) để phân chia khối lệnh.
  * Sử dụng dấu hai chấm (`:`) bắt buộc trước các khối lệnh (if, for,...).
  * Quy tắc đặt tên biến tiêu chuẩn trong Python (khuyến nghị dùng snake_case).
  * Cách ngắt dòng cho biểu thức dài sử dụng dấu gạch chéo ngược (`\`) hoặc cặp ngoặc đơn `()`.

### 3. [bien_va_gan_gia_tri.py](file:///d:/Workspace/University/Python/bien_va_gan_gia_tri.py)
* **Nội dung:** Cách làm việc với biến và gán giá trị.
* **Chi tiết:**
  * Gán giá trị động (Dynamic Typing) trong Python.
  * Sử dụng hàm `type()` để kiểm tra kiểu và `len()` để đo độ dài.
  * Khái niệm về giá trị đặc biệt `None` (không có giá trị).
  * Nhúng biến và định dạng chuỗi nâng cao với `f-string` (làm tròn số thập phân, tính toán trực tiếp trong chuỗi).

### 4. [multiple_variable_and_swap.py](file:///d:/Workspace/University/Python/multiple_variable_and_swap.py)
* **Nội dung:** Các thao tác nâng cao với nhiều biến.
* **Chi tiết:**
  * Gán giá trị đồng thời cho nhiều biến.
  * Gán cùng một giá trị cho nhiều biến cùng lúc (`x = y = z = 1`).
  * Hoán đổi giá trị giữa 2 hoặc nhiều biến một cách ngắn gọn (`a, b = b, a`).
  * Sử dụng từ khóa `del` để xóa biến giải phóng bộ nhớ.
  * Unpacking (giải nén) dữ liệu từ `List` và `Tuple`.
  * Cách kiểm tra sự tồn tại của biến bằng khối lệnh `try - except NameError`.

### 5. [KieuDuLieuVaToanTu/kieu_so_int_float.py](file:///d:/Workspace/University/Python/KieuDuLieuVaToanTu/kieu_so_int_float.py)
* **Nội dung:** Kiểu số (`int`, `float`) và các toán tử số học.
* **Chi tiết:**
  * Kiểu số nguyên `int` (không giới hạn độ dài trong Python) và số thực `float`.
  * Các toán tử số học cơ bản và thứ tự ưu tiên toán tử (Nhân chia trước, cộng trừ sau, trong ngoặc trước, tính lũy thừa từ phải sang trái).
  * Toán tử gán rút gọn (`+=`, `-=`, `*=`, `/=`, `//=`).
  * Ép kiểu dữ liệu bằng hàm `int()` và `float()`.
  * Một số hàm toán học thông dụng: `round()` (làm tròn số), `abs()` (trị tuyệt đối), `min()`, `max()`.

### 6. [KieuDuLieuVaToanTu/Chuỗi.py](file:///d:/Workspace/University/Python/KieuDuLieuVaToanTu/Chu%E1%BB%97i.py)
* **Nội dung:** Kiểu dữ liệu chuỗi (String) và các phương thức xử lý chuỗi.
* **Chi tiết:**
  * Tạo chuỗi đơn dòng, đa dòng, nối chuỗi (`+`) và nhân chuỗi (`*`).
  * Truy cập ký tự bằng chỉ mục (Indexing) và kỹ thuật cắt chuỗi (Slicing - `[start:end:step]`).
  * Đo độ dài chuỗi bằng hàm `len()`.
  * Các phương thức chuyển đổi định dạng chuỗi: `upper()`, `lower()`, `capitalize()`, `title()`, `strip()`, `lstrip()`, `rstrip()`.
  * Tìm kiếm và thay thế chuỗi bằng `find()`, `count()`, `replace()`, và kiểm tra thành viên bằng từ khóa `in`.
  * Tách và gộp chuỗi bằng phương thức `split()` và `join()`.
  * Hiểu tính chất bất biến (immutable) của chuỗi trong Python.

### 7. [CauTrucReNhanh/If - Elif - Else.py](file:///d:/Workspace/University/Python/CauTrucReNhanh/If%20-%20Elif%20-%20Else.py)
* **Nội dung:** Cấu trúc rẽ nhánh cơ bản trong Python.
* **Chi tiết:**
  * Cấu trúc rẽ nhánh cơ bản với `if`.
  * Cấu trúc hai nhánh `if - else`.
  * Cấu trúc nhiều nhánh `if - elif - else` phân loại học lực học sinh.
  * Kết hợp nhiều điều kiện logic bằng các toán tử `and`, `or`, `not`.

### 8. [CauTrucReNhanh/BieuThucDieuKienNangCao.py](file:///d:/Workspace/University/Python/CauTrucReNhanh/BieuThucDieuKienNangCao.py)
* **Nội dung:** Biểu thức so sánh nâng cao và các kỹ thuật tối ưu hóa điều kiện rẽ nhánh.
* **Chi tiết:**
  * Chained Comparison (So sánh chuỗi liên tục) giúp biểu thức điều kiện gọn gàng hơn.
  * Biểu thức điều kiện viết ngắn trên 1 dòng (Ternary Operator).
  * Sử dụng toán tử `in` / `not in` kiểm tra phần tử trong danh sách hoặc kiểm tra chuỗi con.
  * Thay thế cấu trúc `if-elif` phức tạp bằng toán tử kiểm tra thành viên `in`.
  * Các ứng dụng thực tế: Tính toán BMI và kiểm tra thông tin đăng nhập tài khoản.

### 9. [ListCoBan&For/list_va_for.py](file:///d:/Workspace/University/Python/ListCoBan%26For/list_va_for.py)
* **Nội dung:** Danh sách (List) cơ bản và vòng lặp `for` trong Python.
* **Chi tiết:**
  * Khởi tạo List (chuỗi, số, hỗn hợp, danh sách rỗng) và kiểm tra độ dài với `len()`.
  * Truy cập và chỉnh sửa phần tử bằng chỉ mục dương và âm.
  * Duyệt qua các phần tử trong List bằng vòng lặp `for`.
  * Tạo dãy số linh hoạt với hàm `range()` (`range(stop)`, `range(start, stop)`, `range(start, stop, step)` và đếm ngược).
  * Kết hợp `for`, `range()` và chỉ mục để quản lý danh sách.
  * Sử dụng hàm `enumerate()` lấy đồng thời chỉ mục (index) và giá trị của từng phần tử.

### 10. [ListCoBan&For/while_va_dieu_khien_vong_lap.py](file:///d:/Workspace/University/Python/ListCoBan%26For/while_va_dieu_khien_vong_lap.py)
* **Nội dung:** Vòng lặp `while` và các lệnh điều khiển luồng vòng lặp.
* **Chi tiết:**
  * Sử dụng vòng lặp `while` với biến đếm điều kiện.
  * Phân biệt trường hợp sử dụng giữa vòng lặp `for` và `while`.
  * Lệnh `break` để thoát khỏi vòng lặp lập tức.
  * Lệnh `continue` để bỏ qua lần lặp hiện tại và chuyển sang lần lặp kế tiếp.
  * Lệnh `pass` đóng vai trò là giữ chỗ (placeholder) khi chưa có mã xử lý.
  * Kỹ thuật vòng lặp vô hạn `while True` kết hợp điều kiện thoát với `break`.

### 11. [ListCoBan&For/list_methods.py](file:///d:/Workspace/University/Python/ListCoBan%26For/list_methods.py)
* **Nội dung:** Các phương thức (methods) thao tác với List trong Python.
* **Chi tiết:**
  * Thêm phần tử: `append()`, `insert()`, `extend()` và phân biệt `append` vs `extend`.
  * Xóa phần tử: `remove()`, `pop()`, `pop(index)` và `del`.
  * Sắp xếp và đảo ngược: `sort()`, `sort(reverse=True)`, `sorted()`, `reverse()`, `[::-1]`.
  * Tìm kiếm và đếm: `index()`, `count()`, kiểm tra sự tồn tại với toán tử `in`.
  * Các hàm thống kê: `len()`, `sum()`, `min()`, `max()`, và tính điểm trung bình.
  * Ví dụ ứng dụng thực tế quản lý danh sách sinh viên.

### 12. [TongHopCoBan/input_nguoi_dung.py](file:///d:/Workspace/University/Python/TongHopCoBan/input_nguoi_dung.py)
* **Nội dung:** Nhận dữ liệu đầu vào từ người dùng (User Input) và xử lý ngoại lệ.
* **Chi tiết:**
  * Sử dụng hàm `input()` để nhận dữ liệu từ bàn phím (mặc định luôn trả về kiểu `str`).
  * Chuyển đổi kiểu dữ liệu (Type Casting) bằng `int()`, `float()`.
  * Xử lý lỗi nhập sai kiểu dữ liệu với khối lệnh `try - except ValueError`.
  * Kiểm tra chuỗi rỗng và loại bỏ khoảng trắng thừa với `.strip()`.
  * Kiểm tra miền giá trị hợp lệ của số nhập vào.

### 13. [funtion/funtion.py](file:///d:/Workspace/University/Python/funtion/funtion.py)
* **Nội dung:** Khái niệm và cách định nghĩa Hàm (Functions) trong Python.
* **Chi tiết:**
  * Định nghĩa hàm cơ bản với từ khóa `def` và truyền tham số (Parameters).
  * Lệnh `return` trả về giá trị (và dừng hàm ngay lập tức).
  * Trả về nhiều giá trị cùng lúc (Multiple Return Values / Tuple Unpacking).
  * Viết tài liệu hướng dẫn Docstring (`"""..."""`) cho hàm.
  * Phân biệt hàm có `return` và hàm không có `return` (mặc định trả về `None`).

### 14. [funtion/tham_so_nang_cao.py](file:///d:/Workspace/University/Python/funtion/tham_so_nang_cao.py)
* **Nội dung:** Các loại tham số nâng cao trong hàm.
* **Chi tiết:**
  * Tham số mặc định (Default Parameters) và quy tắc thứ tự khai báo.
  * Đối số theo tên (Keyword Arguments) giúp truyền tham số không phụ thuộc vị trí.
  * Sử dụng `*args` để nhận số lượng đối số tùy ý dưới dạng `Tuple`.
  * Giải nén danh sách/tuple (`Unpacking *nums`) trực tiếp vào lời gọi hàm.

### 15. [funtion/pham_vi_bien_va_lamda.py](file:///d:/Workspace/University/Python/funtion/pham_vi_bien_va_lamda.py)
* **Nội dung:** Phạm vi của biến (Scope) và hàm ẩn danh Lambda.
* **Chi tiết:**
  * Biến cục bộ (Local Scope) và biến toàn cục (Global Scope), cách thay đổi với từ khóa `global`.
  * Quy tắc tra cứu biến LEGB (Local -> Enclosing -> Global -> Built-in).
  * Hàm ẩn danh Lambda (Anonymous Functions) viết ngắn gọn trên 1 dòng.
  * Ứng dụng Lambda làm `key` khi sắp xếp danh sách với `sorted()`.
  * Kết hợp Lambda với các hàm xử lý tập hợp `map()` và `filter()`.

### 16. [ListNangCao_Tuple/ListConprehension.py](file:///d:/Workspace/University/Python/ListNangCao_Tuple/ListConprehension.py)
* **Nội dung:** Khởi tạo danh sách bằng List Comprehension.
* **Chi tiết:**
  * Cú pháp tạo list nhanh viết gọn trong 1 dòng.
  * Lọc phần tử bằng điều kiện `if`.
  * Thay đổi giá trị phần tử với cấu trúc `if-else` trong list comprehension.
  * Phép toán trên danh sách lồng nhau (ma trận) và trải phẳng danh sách (flattening).

### 17. [ListNangCao_Tuple/Tuple, enumerate, zip, sorted.py](file:///d:/Workspace/University/Python/ListNangCao_Tuple/Tuple,%20enumerate,%20zip,%20sorted.py)
* **Nội dung:** Kiểu dữ liệu Tuple (Bất biến) và kỹ thuật giải nén Unpacking.
* **Chi tiết:**
  * Khởi tạo Tuple, tính chất bất biến của Tuple.
  * Kỹ thuật giải nén cơ bản (Unpacking Tuple).
  * Sử dụng toán tử `*` gom các phần tử còn lại (Extended Unpacking).

### 18. [ListNangCao_Tuple/slicing_nang_cao.py](file:///d:/Workspace/University/Python/ListNangCao_Tuple/slicing_nang_cao.py)
* **Nội dung:** Cắt lát danh sách nâng cao (Slicing) và sao chép danh sách.
* **Chi tiết:**
  * Cú pháp slicing đầy đủ `[start:stop:step]` và các chỉ số âm.
  * Thay thế phần tử trong danh sách bằng slicing.
  * Xử lý List lồng nhau (List 2D).
  * Bẫy sao chép danh sách (Copy vs Reference), phân biệt sao chép nông (shallow copy) và sao chép sâu (deepcopy).

### 19. [Dictiondary & Set/dictionary.py](file:///d:/Workspace/University/Python/Dictiondary%20%26%20Set/dictionary.py)
* **Nội dung:** Cấu trúc dữ liệu Từ điển (Dictionary) trong Python.
* **Chi tiết:**
  * Khởi tạo Dictionary bằng ngoặc nhọn `{}` hoặc hàm dựng `dict()`.
  * Truy cập, cập nhật giá trị và thêm cặp key-value mới.
  * Truy cập an toàn bằng phương thức `.get()` tránh lỗi `KeyError`.
  * Xóa phần tử bằng `del` và `.pop()`.
  * Duyệt qua Dictionary sử dụng `.keys()`, `.values()`, `.items()`.
  * Các phương thức nâng cao: `.setdefault()`, `.update()` gộp từ điển.
  * Ứng dụng đếm tần suất xuất hiện của từ trong chuỗi văn bản.

### 20. [Dictiondary & Set/dict_comprehension_and_nested_dict.py](file:///d:/Workspace/University/Python/Dictiondary%20%26%20Set/dict_comprehension_and_nested_dict.py)
* **Nội dung:** Cấu trúc từ điển lồng nhau (Nested Dictionary) và Dictionary Comprehension.
* **Chi tiết:**
  * Tạo từ điển nhanh bằng Dictionary Comprehension với các điều kiện lọc.
  * Ghép cặp 2 danh sách thành từ điển bằng `zip()`.
  * Khởi tạo, truy cập và cập nhật từ điển lồng nhau nhiều cấp.
  * Sử dụng `defaultdict(list)` để nhóm các phần tử và gom nhóm hóa đơn.

### 21. [Dictiondary & Set/Set.py](file:///d:/Workspace/University/Python/Dictiondary%20%26%20Set/Set.py)
* **Nội dung:** Cấu trúc dữ liệu Tập hợp (Set) trong Python.
* **Chi tiết:**
  * Khởi tạo tập hợp Set (không trùng lặp, không thứ tự) và ép kiểu từ danh sách.
  * Phân biệt cách khai báo dictionary rỗng `{}` và tập hợp rỗng `set()`.
  * Thêm phần tử vào tập hợp bằng phương thức `add()`.

### 22. [ThucHanh/QuanLySinhVien.py](file:///d:/Workspace/University/Python/ThucHanh/QuanLySinhVien.py)
* **Nội dung:** Bài thực hành tính điểm trung bình học tập của sinh viên.
* **Chi tiết:**
  * Tính điểm trung bình (Average Score) từ danh sách điểm của từng sinh viên.
  * Sắp xếp danh sách sinh viên giảm dần theo điểm trung bình bằng `sorted()` và hàm ẩn danh `lambda`.

### 23. [ThucHanh/dem tu.py](file:///d:/Workspace/University/Python/ThucHanh/dem%20tu.py)
* **Nội dung:** Bài thực hành đếm tần suất xuất hiện của từ trong chuỗi.
* **Chi tiết:**
  * Sử dụng thư viện `collections.Counter` để thống kê số lần xuất hiện của các từ.
  * Xử lý ngoại lệ đầu vào bằng `raise TypeError` khi dữ liệu không phải kiểu chuỗi (`str`).

---
Chúc bạn học tập Python thật hiệu quả! 🚀











