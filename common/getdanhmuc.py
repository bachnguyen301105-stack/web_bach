import mysql.connector
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def get_all_danhmuc():
    """Hàm lấy danh sách tất cả danh mục từ bảng danhmuc"""
    try:
        # Kết nối MySQL
        connection = connect_mysql()
        if connection is None:
            return

        if connection.is_connected():
            cursor = connection.cursor()
            sql = "SELECT id_danhmuc, ten_danhmuc, mo_ta FROM danhmuc"
            cursor.execute(sql)
            rows = cursor.fetchall()

            print("📦 Danh sách danh mục:")
            for row in rows:
                print(f"ID: {row[0]} | Tên: {row[1]} | Mô tả: {row[2]}")

            return rows

    except Error as e:
        print("❌ Lỗi khi lấy danh sách danh mục:", e)
        return []

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
