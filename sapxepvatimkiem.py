from nhanvien import NhanVien
def list_nhan_vien():
    nv = [NhanVien('Trịnh Quốc Dân', 18, 100000),
          NhanVien('Phạm Phước Bảo Tín', 20, 150000),
          NhanVien('Văn Khiêm Chương ', 15, 130000),
          NhanVien(' Trần Tùng Dương ', 19, 250000)]
    return nv
def giam_dan():
    nv=sorted(list_nhan_vien(),reverse=True)
    for item in nv:
        print(item)
def main():
    giam_dan()
if __name__=='__main__':
    main()
