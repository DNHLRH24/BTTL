from nhanvien import NhanVien
import os
import pickle
def luu_list_nhanvien(thumuc: str, ten_taptin: str, objs: NhanVien):
    with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
        pickle.dump(objs, f)
    print('Ket thuc qua trinh luu du lieu')
def main():
    path = 'C:\doan\chuong3'
    filename = 'nhanvien.dat'
    nv = [NhanVien('Trịnh Quốc Dân', 18, 100000),
          NhanVien('Phạm Phước Bảo Tín', 20, 150000),
          NhanVien('Văn Khiêm Chương ', 15, 130000),
          NhanVien(' Trần Tùng Dương ', 19, 250000)]
    luu_list_nhanvien(path,filename,nv)
if __name__=='__main__':
    main()