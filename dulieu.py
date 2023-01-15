from nhanvien import NhanVien
def list_nhan_vien():
    nv = [NhanVien('Trịnh Quốc Dân', 18, 100000),
          NhanVien('Phạm Phước Bảo Tín', 20, 150000),
          NhanVien('Văn Khiêm Chương ', 15, 130000),
          NhanVien(' Trần Tùng Dương ', 19, 250000)]
    for item in nv:
        print(item)
    return nv
def main():
    list_nhan_vien()
if __name__=='__main__':
    main()
