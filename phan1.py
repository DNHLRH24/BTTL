import random
import os
import pickle
import random
n = int(input('nhap n:'))
a = int(input('nhap a:'))
b = int(input('nhap b:'))
def list_so_thuc(a,b):
    x=[(b-a)*random.random() +a for i in range(n)]
    return x
def list_tang_dan(x):
    x=sorted(list_so_thuc(a,b),reverse=False)
    return x
def list_giam_dan(x):
    x=sorted(list_so_thuc(a,b),reverse=True)
    return x
c=int(input('nhap c:'))
def tim_kiem_trong_list(c):
    try:
      print('vi tri cua c la ', x.index(c))
    except :
      print('khong tim thay')
def luu_list_vao_tap_tin(x):
    path='C:/nnlttqd/doan'
    filename='listsothuc.txt'
    with open(os.path.join(path,filename),'wb') as x :
        pickle.dump(list_so_thuc(a,b),x)
        print('ket thuc qua trinh luu')
def main():
    x=list_so_thuc(a,b)
    print(x)
    print(list_tang_dan(x))
    print(list_giam_dan(x))
    tim_kiem_trong_list(c)
    luu_list_vao_tap_tin(x)
if __name__ == '__main__':
    main()