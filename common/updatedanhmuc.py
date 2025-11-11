import mysql.connector
from mysql.connector import Error

from ketnoidb.ketnoi_mysql import connect_mysql


def update_danhmuc(id_danhmuc, ten_moi, mo_ta_moi):
    """Hàm cập nhật tên và mô tả danh mục theo ID"""
    try:
        # Kết nối MySQL
        connection = connect_mysql()
        if connection  is None:
            return 

        if connection.is_connected():
            cursor = connection.cursor()
            sql = """
                UPDATE danhmuc
                SET ten_danhmuc = %s, mo_ta = %s
                WHERE id_danhmuc = %s
            """
            values = (ten_moi, mo_ta_moi, id_danhmuc)
            cursor.execute(sql, values)
            connection.commit()

            if cursor.rowcount > 0:
                print(f"✅ Đã cập nhật danh mục ID = {id_danhmuc}")
            else:
                print(f"⚠️ Không tìm thấy danh mục có ID = {id_danhmuc}")

    except Error as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
