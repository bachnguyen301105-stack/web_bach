import mysql.connector
from mysql.connector import Error

def connect_mysql():
    """Hàm kết nối MySQL và trả về đối tượng connection"""
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Địa chỉ máy chủ MySQL
            user='root',           # Tên đăng nhập MySQL
            password='',           # Mật khẩu (nếu dùng XAMPP thì thường để trống)
            database='web_thuoc'   # Tên cơ sở dữ liệu
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi khi kết nối MySQL:", e)
        return None
