# __Python cơ bản__

## 1. Variable (Biến)
Biến trong python không cần phải khai báo kiểu dữ liệu
```python
a = 4
b = 5
print(a+b)
```
Khi chạy đoạn lệnh trên, ta sẽ được kết quả:
```
9
```
## 2. Method (Phương thức)
Sử dụng cú pháp 
```python
def name_method(arguments):
pass
```
Với `name_method` là tên phương thức, `arguments` là các tham số, `pass` có nghĩa là không làm gì (hoặc thay `pass` bằng các câu lệnh khác)

Ví dụ:
```py
def plus(a,b):
    return(a+b)
print(plus(3,4))

```
Chạy đoạn lệnh trên ta được kết quả sau:
```
7
```
## 3. Lists, Tuples, Sets
`List` là kiểu dữ liệu có thể biến đổi (mutable), bạn có thể sử dụng phương thức như `append()` để thêm phần tử vào `List`, hoặc sử dụng phương thức `remove()` để xóa các phần tử ra khỏi `List` mà không làm tạo ra thêm một thực thể `List` khác trên bộ nhớ. Khi viết `List` ta dùng cặp dấu [ ].

`Tuples` là một kiểu dữ liệu bất biến (immutable), khác với `List` mọi thao tác cập nhập trên `Tuple` đều tạo ra một thực thể mới trên bộ nhớ (memory). Khi viết `Tuple` ta dùng cặp dấu ( ).

`Sets` chứa các phần tử __duy nhất__ và __không có thứ tự__. Các phần tử trong `Set` phân cách nhau bởi dấu phẩy và nằm trong cặp dấu { }. Khác với `Tuple`, các phần tử trong `Set` có thể được thêm (Add) hoặc xóa (Delete). Tạo `Set` rỗng đôi chút khó khăn; không giống `List` và `Tuple`, nếu ta dùng cặp dấu { } sẽ tạo một `Dictionary`. Ta dùng lệnh `set()` không đối số để tạo `Set` rỗng

Ví dụ:
```py
a = [1,2,3,4,5]
b = (1,2,3,4)
print(a)
print(b)
print("Address a: ", hex(id(a)))
print("Address b: ", hex(id(b)))

a = a.remove(2)
print(a)
print("Address a (after remove): ", hex(id(a)))

b = b + (9, 10)
print(b)
print("Address b (after add): ", hex(id(b)))
```

Chạy đoạn lệnh trên ta được kết quả sau:
```
[1,2,3,4,5]
(1,2,3,4)
Address a:  0x24db0ec1200
Address b:  0x24db0ec6860
[1, 3, 4, 5]
Address a (after remove):  0x2397fe51200
(1, 2, 3, 4, 9, 10)
Address b (after add):  0x2397fe4c4c0
```

_Các phương thức của `List`_:

>+ `append()`: Thêm phần tử vào cuối `list`.
>+ `extend()`: Thêm tất cả phần tử của `list` hiện tại vào list khác.
>+ `insert()`: Chèn một phần tử vào `index` cho trước.
>+ `remove()`: Xóa phần tử khỏi `list`.
>+ `pop()`: Xóa phần tử khỏi `list` và trả về phần tử tại `index` đã cho.
>+ `clear()`: Xóa tất cả phần tử của `list`.
>+ `index()`: Trả về `index` của phần tử phù hợp đầu tiên.
>+ `count()`: Trả về số lượng phần tử đã đếm được trong `list` như một đối số.
>+ `sort()`: Sắp xếp các phần tử trong `list` theo thứ tự tăng dần.
>+ `reverse()`: Đảo ngược thứ tự các phần tử trong `list`.
>+ `copy()`: Trả về bản sao của `list`.

_Các hàm tích hợp với `List`_

>+ `all()`: Trả về giá trị `True` nếu tất cả các phần tử của `list` đều là `true` hoặc `list` rỗng.
>+ `any()`: Trả về True khi bất kỳ phần tử nào trong `list` là true. Nếu `list` rỗng hàm trả về giá trị False.
>+ `enumerate()`: Trả về đối tượng `enumerate`, chứa `index` và giá trị của tất cả các phần tử của `list` dưới dạng `tuple`.
>+ `len()`: Trả về độ dài (số lượng phần tử) của `list`.
>+ `list()`: Chuyển đổi một đối tượng có thể lặp (`tuple`, `string`, `set`, `dictionary`) thành `list`.
>+ `max()`: Trả về phần tử lớn nhất trong `list`.
>+ `min()`: Trả về phần tử nhỏ nhất trong `list`.
>+ `sorted()`: Trả về list mới đã được sắp xếp.
>+ `sum()`: Trả về tổng của tất cả các phần tử trong `list`.

_Phương thức của `Tuple`_:
>+ `count(x)`: Đếm số phần tử x trong `tuple`.
>+ `index(x)`: Trả về giá trị `index` của phần tử x đầu tiên mà nó gặp trong `tuple`.

_Các hàm tích hợp trong `Tuple` (Tương tự như `List`)_:
>+ `all()`: Trả về giá trị `True` nếu tất cả các phần tử của `tuple` là `true` hoặc `tuple` rỗng.
>+ `any()`: Trả về True nếu bất kỳ phần tử nào của `tuple` là `true`, nếu `tuple` rỗng trả về `False`.
>+ `enumerated()`: Trả về đối tượng `enumerate` (liệt kê), chứa cặp `index` và giá trị của tất cả phần tử của tuple.
>+ `len()`: Trả về độ dài (số phần tử) của `tuple`.
>+ `max()`: Trả về phần tử lớn nhất của `tuple`.
>+ `min()`: Trả về phần tử nhỏ nhất của `tuple`.
>+ `sorted()`: Lấy phần tử trong `tuple` và trả về list mới được sắp xếp (`tuple` không sắp xếp được).
>+ `sum()`: Trả về tổng tất cả các phần tử trong tuple.
>+ `tuple()`: Chuyển đổi những đối tượng có thể lặp (`list`, `string`, `set`, `dictionary`) thành `tuple`.

_Các phương thức dùng trên `Set`_:
>+ `add()`: Thêm một phần tử vào `set`.
>+ `clear()`: Xóa tất cả phần tử của `set`.
>+ `copy()`: Trả về bản sao chép của `set`.
>+ `difference()`: Trả về `set` mới chứa những phần tử khác nhau của 2 hay nhiều `set`.
>+ `difference_update()`: Xóa tất cả các phần tử của `set` khác từ `set` này.
>+ `discard()`: Xóa phần tử nếu nó có mặt trong `set`.
>+ `intersection()`: Trả về `set` mới chứa phần tử chung của 2 `set`.
>+ `intersection_update()`: Cập nhật `set` với phần tử chung của chính nó và `set` khác.
>+ `isdisjoint()`: Trả về `True` nếu 2 `set` không có phần tử chung.
>+ `issubset()`: Trả về `True` nếu `set` khác chứa `set` này.
>+ `issuperset()`: Trả về `True` nếu `set` này chưa set khác.
>+ `pop()`: Xóa và trả về phần tử ngẫu nhiên, báo lỗi `KeyError` nếu `set` rỗng.
>+ `remove()`: Xóa phần tử từ `set`. Nếu phần tử đó không có trong `set` sẽ báo lỗi `KeyError`.
>+ `symmetric_difference()`: Trả về `set` mới chứa những phần tử không phải là phần tử chung của 2 `set`.
>+ `symmetric_difference_update()`: Cập nhật `set` với những phần tử khác nhau của chính nó và `set` khác.
>+ `union()`: Trả về `set` mới là hợp của 2 `set`.
>+ `update()`: Cập nhật `set` với hợp của chính nó và `set` khác.

_Các hàm trên `Set`_:

>Các hàm thường dùng trên set bao gồm `all()`, `any()`, `enumerate()`, `len()`, `max()`, `min()`, `sorted()`, `sum()`. Chức năng của những hàm này khá giống với khi bạn sử dụng trên `list`, `tuple`.

__List comprehension:__

`List comprehension` là một biểu thức đi kèm với lệnh `for` hoặc lệnh `if` được đặt trong cặp dấu ngoặc vuông [ ]

_Ví dụ_:
```py
test = [2 ** x for x in range(9) if x > 3]
print(test)

noi_list = [x+y for x in ['Chuối ','Táo '] for y in ['có màu xanh','có màu vàng']]
print(noi_list)
```
Sau khi chạy chương trình trên ta được kết quả như sau:
```
[16, 32, 64, 128, 256]
['Chuối có màu xanh', 'Chuối có màu vàng', 'Táo có màu xanh', 'Táo có màu vàng']
```
## 4. Loop (Vòng lặp)
Ta có thể dùng các lệnh lặp `For` (lặp với số vòng lặp xác định) hoặc `While` (lặp với số vòng lặp không xác định) để tạo vòng lặp.

_Ví dụ:_
```python
num = [1, 2, 3, 4, 5]
color = ("red", "blue", "white", "yellow", "black")
for number in num:
    print(number)
for x in range(0,len(color)):
    print(color[x])   
i = 0
while(i<5):
    print(i)
    i=i+1 
```
Thực hiện chạy đoạn lệnh trên ta được kết quả như sau: 
```
1
2
3
4
5
red
blue
white
yellow
black
0
1
2
3
4
```

## 5. If (Câu lệnh rẽ nhánh)

Lệnh `If` sex kiểm tra điều kiện. Nếu điều kiện trả về `True`, khối lệnh sau `If` sẽ được thực hiện.

_Ví dụ:_
```py
num = ["1", "2", "3", "4", "5"]
a = input("Nhap so bat ky? :")
if a in num:
    print(a, " co trung num")
else:
    print(a, " khong co trong num")
```
Kết quả sau khi thực hiện chạy đoạn chương trình trên:
```
Nhap so bat ky? :2
2 co trung num

Nhap so bat ky? :7
7 khong co trung num
```
## 6. Dictionary
`Dictionary` là tập hợp các cặp khóa giá trị không có thứ tự. Nó thường được sử dụng khi chúng ta có một số lượng lớn dữ liệu. Các `dictionary` được tối ưu hóa để trích xuất dữ liệu với điều kiện bạn phải biết được khóa để lấy giá trị.

+ `Dictionary` được định nghĩa trong dấu ngoặc nhọn {} với mỗi phần tử là một cặp theo dạng `key:value`. `Key` và `value` này có thể là bất kỳ kiểu dữ liệu nào. Bạn cũng có thể tạo `dictionary` bằng cách sử dụng hàm `dict()` được tích hợp sẵn.
+ __Truy cập phần tử của dictionary__

    Các kiểu dữ liệu lưu trữ khác sử dụng `index` để truy cập vào các giá trị thì `dictionary` sử dụng các `key`. `Key` có thể được sử dụng trong cặp dấu ngoặc vuông hoặc sử dụng `get()`.

+ __Thay đổi, thêm phần tử cho dictionary__

    `Dictionary` có thể thay đổi, nên có thể thêm phần tử mới hoặc thay đổi giá trị của các phần tử hiện có bằng cách sử dụng toán tử gán. Nếu key đã có, giá trị sẽ được cập nhật, nếu là một cặp `key`: `value` mới thì sẽ được thêm thành phần tử mới.
+ **Xóa phần tử từ dictionary**
    Có thể xóa phần tử cụ thể của `dictionary` bằng cách sử dụng `pop()`, nó sẽ phần tử có `key` đã cho và trả về giá trị của phần tử. `popitem()` có thể xóa và trả về một phần tử tùy ý dưới dạng (`key`, `value`). Tất cả các phần tử trong `dictionary` có thể bị xóa cùng lúc bằng cách dùng `clear()`. Ngoài ra, từ khóa `del` cũng có thể dùng để xóa một phần tử hoặc toàn bộ `dictionary`.

_Ví dụ_:
```python
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
```
Thực hiện chạy chương trình trên ta được kết quả như sau:
```
<class 'dict'> <class 'dict'> <class 'dict'>
dict1[1] =  A
dict2[trái] =  Xoài
{1: 'C', 2: 'B'} {'quả': 'Táo', 'trái': 'Xoài', 3: 'Nho'}
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
3
{1: 1, 2: 2, 4: 4, 5: 5, 6: 6}
{1: 1, 4: 4, 5: 5, 6: 6}
(6, 6)
{}
```
>__Các phương thức và hàm cho dictionary__:
>+ `clear()`	Xóa tất cả phần tử của `dictionary`.
>+ `copy()`	Trả về một bản sao shollow copy của `dictionary`.
>+ `fromkeys(seq[,v])`	Trả về `dictionary` mới với key từ `seq` và `value` bằng `v` (default là `None`).
>+ `get(key[,d])`	Trả về giá trị của `key`, nếu `key` không tồn tại, trả về d. (default là `None`).
>+ `items()`	Trả lại kiểu xem mới của các phần tử trong `dictionary` (`key`, `value`).
>+ `keys()`	Trả về kiểu xem mới của các `key` trong dictionary.
>+ `pop(key[,d])`	Xóa phần tử bằng `key` và trả về giá trị hoặc `d` nếu `key` không tìm thấy. Nếu `d` không được cấp, `key` không tồn tại thì sẽ tạo lỗi `KeyError`.
>+ `popitem()`	Xóa và trả về phần tử bất kỳ ở dạng (`key`, `value`). Tạo lỗi `KeyError` nếu `dictionary` rỗng.
>+ `setdefault(key,[,d])`	Nếy `key` tồn tại trả về `value` của nó, nếu không thêm `key` với `value` là `d` và trả về `d` (default là `None`).
>+ `update([other])`	Cập nhật `dictionary` với cặp `key/value` từ `other`, ghi đè lên các `key` đã có.
>+ `values()`	Trả về kiểu view mới của `value` trong `dictionary`.
>Các hàm tích hợp như `all()`, `any()`, `len()`, `cmp()`, `sorted()`,... thường được sử dụng với `dictionary` để thực hiện những nhiệm vụ khác nhau.

__Dictionary comprehension trong Python__
+ `Dictionary comprehension` là cách đơn giản, rút gọn để tạo `dictionary` mới từ một vòng lặp trong `Python`. Câu lệnh sẽ bao gồm một cặp biểu thức `(key:value)` cùng câu lệnh `for` hoặc `if`, tất cả đặt trong dấu { }
_Ví dụ_:
```py
# tạo dictionary gồm các số lẻ < 20
le = {x: 2*x+1 for x in range(10)}
print(le)
```
Ta được kết quả:
```
{0: 1, 1: 3, 2: 5, 3: 7, 4: 9, 5: 11, 6: 13, 7: 15, 8: 17, 9: 19}
```
## 7. Hướng đối tượng trong Python

__Class và Object__

Cách tạo một class
```python
class Class_Name:
    'docstring'
    pass
```
Để định nghĩa một class ta dùng từ khóa `class`, tiếp sau là tên class và dấu hai chấm( : ). Dòng đầu tiên trong thân của lớp là chuỗi (string) mô tả ngắn gọn về lớp này (Không bắt buộc), bạn có thể truy cập vào chuỗi này thông qua `Class_Name.__doc__ .` Trong thân của lớp bạn có thể khai báo các thuộc tính, phương thức (Method) và các phương thức khởi tạo (Constructor).

Ví dụ:
```python
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

```
Sau khi thực hiện chương trình trên, kết quả trên màn hình:

```
John - lop 10
[{'subject': 'Math', 'point': 10}, {'subject': 'Physical', 'point': 9.5}]  
Adam - lop 10
[{'subject': 'Bio', 'point': 8}, {'subject': 'Math', 'point': 9.5}]        
John have average point: 9.75
Adam have average point: 8.7

```

__Kế thừa trong python__

Kế thừa là một khía cạnh quan trọng của mô hình lập trình hướng đối tượng. Kế thừa cung cấp khả năng sử dụng lại mã cho chương trình vì chúng ta có thể sử dụng một lớp hiện có để tạo một lớp mới thay vì tạo nó từ đầu.

Trong kế thừa, lớp con có được các thuộc tính và có thể truy cập tất cả các thành viên dữ liệu và các hàm được định nghĩa trong lớp cha. Một lớp con cũng có thể cung cấp việc triển khai cụ thể cho các hàm của lớp cha. Trong bài này, chúng ta sẽ thảo luận chi tiết về kế thừa.

Trong python, một lớp dẫn xuất (hay còn gọi là lớp con - sub-class) có thể kế thừa lớp cơ sở (lớp cha - super-class) bằng cách chỉ đề cập đến cơ sở trong ngoặc sau tên lớp dẫn xuất. Sau đây là cú pháp để một lớp cơ sở kế thừa lớp dẫn xuất.

Cú pháp:
```py
class derived_class(base class):
    <class_suite>
```
Ví dụ:
```py
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
```
Kết quả màn hình:
```
Toyota có chủ sở hữu là Trung, trọng lượng: 56 kg, chiều cao: 1.5 m, giá bán: 1450 đồng
```

__Decorator trong Python__

Decorator là một hàm nhận tham số đầu vào là một hàm khác và mở rộng tính năng cho hàm đó mà không thay đổi nội dung của nó. Hiểu một cách cơ bản nhất, Decorator là một hàm có thể nhận các hàm khác, cho phép bạn chạy một số đoạn code trước hoặc sau hàm chính mà không thay đổi kết quả.

Ví dụ:
```py
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
    
```
Kết quả:
```
Decorator!!!
Test!!!
Afetr Decorator!!!
```
___


Tham khảo tại: 
+ <https://niithanoi.edu.vn/instance-class-va-static-method-trong-python.html>
+ <https://quantrimang.com/gioi-thieu-qua-ve-chuoi-so-list-trong-python-140881#mcetoc_1bs0pu9a20>
+ <https://viettuts.vn/python/ke-thua-trong-python>