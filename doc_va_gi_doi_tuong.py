from student import SinhVien
import os
import pickle

def ghi_sinhvien(thumuc : str,ten_taptin:str,obj):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(obj, f)
            print('hoan thanh qua trinh gi du lieu vao tap tin ')
    except Exception as e:
        print('xay ra loi trong qua trinh tai file ')
def doc_sinhvien(thumuc, ten_taptin: str)  -> SinhVien:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            sv= pickle.load(f)
        return sv
    except Exception as e :
        return None
def main() :
    path = 'C:/dan/data'
    filename= 'sinhvien2.dat'
    sv1 =SinhVien('Quoc Dan',2003,80.0)
    ghi_sinhvien(path,filename,sv1)
    noidung = doc_sinhvien(path,filename)
    print('noidung ')
    print('ket thuc chuong trinh ')
if __name__== '__main__':
    main()




