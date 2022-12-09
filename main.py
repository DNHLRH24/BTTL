class SinhVien:
    def __init__(self,fullname,yob,score):
        self.hoten=fullname
        self.namsinh=yob
        self.dtb=score
    def __str__(self):
        message= 'hoten:'+self.hoten+';nam sinh :'+str(self.namsinh)+';dtb:'+str(self.dtb)+']'
        return message
def main():
    sv1=SinhVien('le anh duy',2004,10)
    sv2=SinhVien('ho tang nhat hieu ',2005,11)
    print(sv1)
    print(sv2)
if __name__== '__main__':
    main()