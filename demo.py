# Biến
a = 4
b = 5
print(a+b)

# Method
def plus(a,b):
    return(a+b)
print(plus(3,4))

# List và Tuple
a = [1,2,3,4,5]     # Tạo list a
b = (1,2,3,4)       # Tạo tuple b
print(a)
print(b)

# xuất địa chỉ hex của a, b
print("Address a: ", hex(id(a)))
print("Address b: ", hex(id(b)))

# remove số ở vị trí 2 trong a và xuất lại địa chỉ a
a = a.remove(2)
print(a)
print("Address a (after remove): ", hex(id(a)))
# thêm 9, 10 vào b và xuất lại địa chỉ b
b = b + (9, 10)
print(b)
print("Address b (after add): ", hex(id(b)))

# List comprehension
test = [2 ** x for x in range(9) if x > 3]                # tạo list test có điều kiện
print(test)

# Tạo list mới bằng việc nối 2 mảng khác nhau
noi_list = [x+y for x in ['Chuối ','Táo '] for y in ['có màu xanh','có màu vàng']]
print(noi_list)

# Loop
num = [1, 2, 3, 4, 5]
color = ("red", "blue", "white", "yellow", "black")
for number in num:                  # in các phần tử của num
    print(number)
for x in range(0,len(color)):       # in các phần tử của color
    print(color[x])   

# Lặp while in các phần tử nhỏ hơn 5
i = 0
while(i<5):
    print(i)
    i=i+1 

# If
num = ["1", "2", "3", "4", "5"]                 # khởi tạo list num
a = input("Nhap so bat ky? :")                  # nhập a
if a in num:                                    # nếu a có trong num
    print(a, " co trung num")                   
else:                                           # còn không thì
    print(a, " khong co trong num")

# Dictionary
# định nghĩa, truy cập phần tử dictionary
dict1 = {1: 'A',2: 'B'}
dict2 = dict({'quả': 'Táo', 'trái': 'Xoài'})
dict3 = dict([('mau1', 'Red'), (2,'Black')])
dict4 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
print(type(dict1),type(dict2), type(dict3))
print("dict1[1] = ", dict1.get(1)) 
print("dict2[trái] = ",dict2['trái'])

# thay đổi, thêm phần tử
dict1[1] = 'C'
dict2[3] = 'Nho'
print(dict1, dict2)

# xóa phần tử 
print(dict4)
print(dict4.pop(3))
print(dict4)
del dict4[2]
print(dict4)
print(dict4.popitem())
dict4.clear()
print(dict4)

# tạo dictionary gồm các số lẻ < 20
le = {x: 2*x+1 for x in range(10)}
print(le)