# __Python Flask__

Flask là một micro web framework được viết bằng Python, không yêu cầu tool hay thư viện cụ thể nào. Flask luôn hỗ trợ các thành phần tiện ích mở rộng cho ứng dụng như tích hợp cơ sở dữ liệu, xác thực biểu mẫu, xử lý upload, các công nghệ xác thực, template, email, RESTful, ..., chỉ khác là khi nào bạn muốn thì bạn mới đưa vào thôi. Người dùng có thể tập trung xây dựng web application ngay từ đầu trong một khoảng thời gian rất ngắn và có thể phát triển quy mô của ứng dụng theo yêu cầu.


## 1. Khởi tạo và kích hoạt môi trường ảo

Cài đặt ứng dụng `virtualenv`
```
pip install virtualenv
```
Khởi tạo môi trường ảo
```
virtualenv hieple
```
Kích hoạt môi trường ảo
```
hieple\Scripts\activate
```
Hoặc sử dụng Anaconda để tạo môi trường ảo:
```
conda.bat create --name <tên mt ảo>
```
Khi được hỏi Proceed hay không? (y/n) thì gõ `y`

Tiếp đó, để kích hoạt môi trường ảo, thực hiện lệnh:
```
conda activate <mt ảo>
```

Để hủy kích hoạt môi trường ảo, thực hiện lệnh:
```
conda deactivate
```

## 2. Cách cài đặt Flask

Bật Terminal và gõ lệnh
``` 
pip install Flask
```

## 3. Hello World
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World "

if __name__ == "__main__":   
    app.run(debug=True)
```

## Routing (Định tuyến)

Sử dụng `route()` để chỉ định mỗi url của người dùng trỏ tới mỗi hàm nhất định.

Ví dụ:
```py

from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def HomePage():
    return 'Home Page'
 

@app.route('/user')
def user():
    return 'User Page'


@app.route('/about')
def about():
    return 'About Page'


if __name__ == '__main__':
    app.run()
```
Khi ta truy cập vào url: http://localhost:5000/home

![image](https://user-images.githubusercontent.com/22864889/97975245-65fcdf80-1dfb-11eb-8200-0990cabf2f81.png)

Khi ta truy cập vào url: http://localhost:5000/user

![image](https://user-images.githubusercontent.com/22864889/97975115-3057f680-1dfb-11eb-81a4-e4337953a45a.png)

Khi ta truy cập vào url: http://localhost:5000/about

![image](https://user-images.githubusercontent.com/22864889/97974010-92aff780-1df9-11eb-84fd-b4af71b0fdc1.png)


Sau khi chạy chương trình trên, trang web sẽ được hiển thị ở: http://127.0.0.1:5000/

Kết quả như sau

![image](https://user-images.githubusercontent.com/22864889/97858075-34b7dd00-1d31-11eb-9c65-a44834fb28fe.png)

## 4. Restful API

RESTful API là một tiêu chuẩn dùng trong việc thiết kế API cho các ứng dụng web (thiết kế Web services) để tiện cho việc quản lý các resource. Nó chú trọng vào tài nguyên hệ thống (tệp văn bản, ảnh, âm thanh, video, hoặc dữ liệu động…), bao gồm các trạng thái tài nguyên được định dạng và được truyền tải qua HTTP.

Cùng nhau tìm hiểu một vài điều mới nhé: 
> API (Application Programming Interface) là một tập các quy tắc và cơ chế mà theo đó, một ứng dụng hay một thành phần sẽ tương tác với một ứng dụng hay thành phần khác. API có thể trả về dữ liệu mà bạn cần cho ứng dụng của mình ở những kiểu dữ liệu phổ biến như JSON hay XML.

> REST (REpresentational State Transfer) là một dạng chuyển đổi cấu trúc dữ liệu, một kiểu kiến trúc để viết API. Nó sử dụng phương thức HTTP đơn giản để tạo cho giao tiếp giữa các máy. Vì vậy, thay vì sử dụng một URL cho việc xử lý một số thông tin người dùng, REST gửi một yêu cầu HTTP như GET, POST, DELETE, vv đến một URL để xử lý dữ liệu.

+ REST:
REST hoạt động chủ yếu dựa vào giao thức HTTP. Các hoạt động cơ bản nêu trên sẽ sử dụng những phương thức HTTP riêng. Phổ biến nhất là:
    
    + GET: Trả về một/một danh sách Resource
    + POST: Tạo mới một Resource 
    + PUT: Cập nhật thông tin cho Resource 
    + DELETE: Xóa một Resource 













