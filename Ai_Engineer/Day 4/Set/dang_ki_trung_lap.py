eventA = {'SV01', 'SV02', 'SV03'}
eventB = {'SV03', 'SV04'}
ma_sv = input("Hãy nhập mã sinh viên của bạn: ")
if (ma_sv in eventA):
    print("Sinh viên đã đăng ký sự kiện A ")
else: 
    eventA.add(ma_sv)
    print("Đã đăng ký thành công ")

print("2. Hủy đăng ký------------")
del_ma = input("Nhập mã sinh viên bạn muốn hủy đăng ký: ")
if (del_ma in eventB):
    eventB.discard(del_ma)
    print("Đã hủy thành công sự kiện! ")
else: 
    print("Mã sinh viên chưa đăng ký sự kiện! ")
print("3. Báo cáo sự kiện:---------")
union = eventA | eventB
print(f"Tổng số sinh viên tham gia ít nhất 1 sự kiện là :{len(union)}")
chung = eventA & eventB
print(f"Danh sách sinh viên thanh gia cả sự kiện A và B là: {chung}")
only_A = eventA - eventB
print(f"Sinh viên chỉ tham gia sự kiện A: {only_A} ")
only_B = eventB - eventA
print(f"Sinh viên chỉ tham gia sự kiện B: {only_B} ")