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

# hướng đối tượng trong python

class Classroom:
    def __init__(self, name):               # phương thức khởi tạo
        self.name = name
        self.prop = []
    def add_sub(self, sub, point):          # phương thức add các thuộc tính    
        self.prop.append({
            'subject': sub,
            'point': point
        })
    
    def average_point(self):                # hàm tính điểm trung bình
        total = 0
        for p in self.prop:
            total += p['point']
        return (total/len(self.prop))
    @classmethod                            # tạo 1 class method
    def grade(cls, classroom):
        new_class = Classroom(classroom.name + " - lop 10")
        return new_class

    @staticmethod                           # tạo 1 static method
    def class_average(classroom):
        return print('{} have average point: {}'.format(classroom.name, classroom.average_point()))

# tạo 2 đối tượng kiểu Clasroom là John và Adam
person1 = Classroom("John")                 
person2 = Classroom("Adam")
person1.add_sub("Math", 10)
person1.add_sub("Physical", 9.5)
person2.add_sub("Bio", 8)
person2.add_sub("Math", 9.5)

print(Classroom.grade(person1).name)
print(person1.prop)
print(Classroom.grade(person2).name)
print(person2.prop)

Classroom.class_average(person1)
Classroom.class_average(person2)


# tạo một class Oto và lớp dẫn xuất Toyota của lớp Oto

class Oto:
        def __init__(self, owner):
                self.owner = owner
class Toyota(Oto):
        def __init__(self, owner, weight, height, price):
                super().__init__(owner)
                self.weight = weight
                self.height = height
                self.price = price
        @classmethod
        def show_info(cls, a):
                print('Toyota có chủ sở hữu là {}, trọng lượng: {} kg, chiều cao: {} m, giá bán: {} đồng'.format(a.owner, a.weight, a.height, a.price))

x = Toyota('Trung', 56, 1.5, 1450)
Toyota.show_info(x)

# Ví dụ về Decorator

def decorator(func):
    def inner():
        print("Decorator!!!")
        func()
        print("Afetr Decorator!!!")
    return inner

@decorator
def test():
    print("Test!!!")

test()
        
