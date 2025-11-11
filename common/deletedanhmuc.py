import mysql
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def delete_danhmuc(id_danhmuc):
    """Hàm xóa danh mục theo ID"""
    try:
        # Kết nối MySQL
        connection = connect_mysql()
        if connection is None:
            return 

        if connection.is_connected():
            cursor = connection.cursor()
            sql = "DELETE FROM danhmuc WHERE id_danhmuc = %s"
            value = (id_danhmuc,)
            cursor.execute(sql, value)
            connection.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã xóa danh mục có ID = {id_danhmuc}")
            else:
                print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")

    except Error as e:
        print("❌ Lỗi khi xóa danh mục:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()