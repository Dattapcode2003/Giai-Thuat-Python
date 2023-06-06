class HocSinh:
    def __init__(self, hoten, dtoan, dvan,lop):
        self.hoten = hoten
        self.dtoan = dtoan
        self.dvan = dvan
        self.lop = lop
    
    def dtb(self):
        return (self.dtoan + self.dvan) / 2
    
    def in_hs(self):
        print(self.hoten, self.dtoan, self.dvan,self.lop)

danh_sach = []
hs = int(input("Nhập số lượng học sinh: "))
for i in range(hs):
    print(f"\nNhập Thông tin học sinh thứ {i+1}:")
    hoten = input("Họ Tên: ")
    lop = input("Lớp:")
    dtoan = float(input("Điểm toán: "))
    dvan = float(input("Điểm văn: "))
    

    h_s = HocSinh(hoten, dtoan, dvan,lop)
    danh_sach.append(h_s)

for h_s in danh_sach:
    h_s.in_hs()
    print("Điểm trung bình của", h_s.hoten, h_s.dtb())