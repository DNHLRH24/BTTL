from nhanvien import NhanVien
import os
import pickle
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
    path = 'C:\doan\chuong3'
    filename = 'nhanvien.dat'
    noidung = doc_tap_tin(path, filename)
    in_list_nhanvien(noidung)
    print('Kết thúc chương trình')
if __name__ =='__main__':
    main()