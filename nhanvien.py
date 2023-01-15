
class NhanVien:
    def __init__(self, fullname: str, yob: int, money: float):
        self.hoten = fullname
        self.tuoi = yob
        self.luong = money
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