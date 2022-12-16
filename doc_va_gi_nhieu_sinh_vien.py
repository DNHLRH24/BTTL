from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc :str , ten_taptin: str , objs: list[SinhVien]):
    try:
        with open(os.path.join(thumuc,ten_taptin), 'wb') as f:
             pickle .dum(objs,f)
             print('hoan thanh qua trinh ghi du lieu vao tap tin ')
    except Exception as e:
             print(' xay ra loi trong qua trinh ghi file')
def doc_sinhvien(thumuc: str , ten_taptin: str ) ->list[SinhVien] :
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
             sv=pickle.load(f)
        return sv
    except Exception as e:
        return None
def in_list_sinhvien(content:list[SinhVien]):
    for item in content:
        print(item)
def main():
    path = 'C:/dan/data'
    filename = 'sinhvien3.dat'
    sv1 =[SinhVien('quoc dan ',2004,10.0),SinhVien('bao tin ',2008,9.0),SinhVien('kiem chuong  ',2009,8.5),SinhVien('tung duong ',2003,9.5)]
    ghi_sinhvien(path,filename,sv1)
    noidung = doc_sinhvien(path,filename)
    in_list_sinhvien(noidung)
    print('ket thuc chuong trinh ')
if __name__ == '__main__':
    main()