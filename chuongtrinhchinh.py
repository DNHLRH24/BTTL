import os
import pickle
#lớp NhanVien có các thuộc tính là hoten, tuoi, luong
class NhanVien:
    def __init__(self, fullname: str, yob: int, money: float):
        self.hoten = fullname
        self.tuoi = yob
        self.luong = money
#dữ liệu cho 1 list các đối tượng thuộc lớp NhanVien
    def __str__(self) -> str:
        message = '[họ tên: ' + self.hoten + '; tuổi: ' \
                  + str(self.tuoi) + '; lương: ' \
                   + str(self.luong) + ']'
        return message
    def __gt__(self, obj):
        return(self.tuoi > obj.tuoi)
    def __ge__(self, obj):
        return(self.tuoi >= obj.tuoi)
    def __lt__(self, obj):
        return(self.tuoi < obj.tuoi)
    def __le__(self, obj):
        return(self.tuoi <= obj.tuoi)
    def __eq__(self, obj):
        return(self.tuoi == obj.tuoi)
#hiển thị list các đối tượng thuộc lớp NhanVien ra màn hình
def list_nhan_vien():
    nv = [NhanVien('Trịnh Quốc Dân', 18, 100000),
          NhanVien('Phạm Phước Bảo Tín', 20, 150000),
          NhanVien('Văn Khiêm Chương ', 15, 130000),
          NhanVien(' Trần Tùng Dương ', 19, 250000)]
    return nv
#sắp xếp list các đối tượng thuộc lớp NhanVien theo chiều giảm dần của độ tuổi
def giam_dan():
    nv=sorted(list_nhan_vien(),reverse=True)
    for item in nv:
        print(item)
#lưu list các đối tượng thuộc lớp NhanVien vào tập tin nhị phân
def luu_list_nhanvien(thumuc: str, ten_taptin: str, objs: NhanVien):
    with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
        pickle.dump(objs, f)
    print('Ket thuc qua trinh luu du lieu')
#đọc list các đối tượng thuộc lớp NhanVien từ tập tin nhị phân
def doc_tap_tin(thumuc: str, ten_taptin: str) -> list[NhanVien]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            nv = pickle.load(f)
        return nv
    except Exception as e:
        return None
def in_list_nhanvien(content: list[NhanVien]):
    for item in content:
        print(item)
def main():
    list_nhan_vien()
    giam_dan()
    path = 'C:\doan\chuong3'
    filename = 'nhanvien.dat'
    nv = [NhanVien('Trịnh Quốc Dân', 18, 100000),
          NhanVien('Phạm Phước Bảo Tín', 20, 150000),
          NhanVien('Văn Khiêm Chương ', 15, 130000),
          NhanVien(' Trần Tùng Dương ', 19, 250000)]
    luu_list_nhanvien(path,filename,nv)
    noidung = doc_tap_tin(path, filename)
    in_list_nhanvien(noidung)
    print('Kết thúc chương trình')
if __name__=='__main__':
    main()
