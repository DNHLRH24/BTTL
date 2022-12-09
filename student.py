class SinhVien:
    def __init__(self,fullname,yob,score):
        self.hoten=fullname
        self.namsinh=yob
        self.dtb=score
    def __str__(self):
        message= 'hoten:'+self.hoten+';nam sinh :'+str(self.namsinh)+';dtb:'+str(self.dtb)+']'
        return message
    def __gt__(self,obj):
        return(self.dtb>obj.dtb)
    def __ge__(self,obj):
        return(self.dtb>=obj.dtb)
    def __lt__(self,obj):
        return(self.dtb<obj.dtb)
    def __le__(self,obj):
        return(self.dtb<=obj.dtb)
    def __eq__(self,obj):
        return(self.dtb==obj.dtb)
