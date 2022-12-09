from student import SinhVien
def main():
    sv=[SinhVien('Trinh Quoc Dan ',2004,10),
        SinhVien('Pham Phuoc Bao Tin',2008,12),
        SinhVien('Van Khiem Chuong',2001,8.0),
        SinhVien('Tran Tung Duong ',2009,7.5)]
    sv=sorted(sv,reverse=True)
    for item in sv:
        print(item)
if __name__== '__main__':
    main()
