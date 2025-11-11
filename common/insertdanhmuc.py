import mysql
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def insert_danhmuc(ten_danhmuc, mo_ta):
    """Hàm thêm danh mục mới vào bảng danhmuc"""
    try:
        # Kết nối MySQL
        connection = connect_mysql()
        if connection is None:
            return

        if connection.is_connected():
            cursor = connection.cursor()
            sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
            values = (ten_danhmuc, mo_ta)
            cursor.execute(sql, values)
            connection.commit()   # Lưu thay đổi
            print("✅ Đã thêm danh mục thành công!")

    except Error as e:
        print("❌ Lỗi khi thêm danh mục:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()