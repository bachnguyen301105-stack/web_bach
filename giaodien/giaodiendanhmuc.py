import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

# ---------------- KẾT NỐI MYSQL ----------------
def connect_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',          # để trống nếu dùng XAMPP
            database='web_thuoc'
        )
        return connection
    except Error as e:
        messagebox.showerror("Lỗi", f"Không thể kết nối MySQL: {e}")
        return None

# ---------------- HÀM HIỂN THỊ DANH MỤC ----------------
def load_data():
    for i in tree.get_children():
        tree.delete(i)
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM danhmuc")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
        cursor.close()
        conn.close()

# ---------------- HÀM THÊM DANH MỤC ----------------
def add_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()
    if ten == "":
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục!")
        return
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        sql = "INSERT INTO danhmuc (ten_danhmuc, mo_ta) VALUES (%s, %s)"
        cursor.execute(sql, (ten, mota))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Thành công", "Đã thêm danh mục mới!")
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        load_data()

# ---------------- HÀM XÓA DANH MỤC ----------------
def delete_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần xóa!")
        return
    id_danhmuc = tree.item(selected)['values'][0]
    confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa ID = {id_danhmuc}?")
    if confirm:
        conn = connect_mysql()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM danhmuc WHERE id_danhmuc = %s", (id_danhmuc,))
            conn.commit()
            cursor.close()
            conn.close()
            messagebox.showinfo("Đã xóa", "Danh mục đã được xóa!")
            load_data()

# ---------------- HÀM CẬP NHẬT DANH MỤC ----------------
def update_danhmuc():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("Chưa chọn", "Vui lòng chọn danh mục cần sửa!")
        return
    id_danhmuc = tree.item(selected)['values'][0]
    ten = entry_ten.get()
    mota = entry_mota.get()
    if ten == "":
        messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập tên danh mục!")
        return
    conn = connect_mysql()
    if conn:
        cursor = conn.cursor()
        sql = "UPDATE danhmuc SET ten_danhmuc=%s, mo_ta=%s WHERE id_danhmuc=%s"
        cursor.execute(sql, (ten, mota, id_danhmuc))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Cập nhật", "Đã sửa danh mục thành công!")
        load_data()

# ---------------- HÀM CHỌN DÒNG ----------------
def on_select(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected)['values']
        entry_ten.delete(0, tk.END)
        entry_mota.delete(0, tk.END)
        entry_ten.insert(0, values[1])
        entry_mota.insert(0, values[2])

# ---------------- GIAO DIỆN TKINTER ----------------
root = tk.Tk()
root.title("Quản lý danh mục")
root.geometry("650x400")
root.resizable(False, False)

# Tiêu đề
tk.Label(root, text="QUẢN LÝ DANH MỤC", font=("Arial", 16, "bold")).pack(pady=10)

# Khung nhập liệu
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

tk.Label(frame_input, text="Tên danh mục:").grid(row=0, column=0, padx=5, pady=5)
entry_ten = tk.Entry(frame_input, width=30)
entry_ten.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Mô tả:").grid(row=1, column=0, padx=5, pady=5)
entry_mota = tk.Entry(frame_input, width=30)
entry_mota.grid(row=1, column=1, padx=5, pady=5)

# Nút chức năng
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)
tk.Button(frame_buttons, text="Thêm", width=10, command=add_danhmuc).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Sửa", width=10, command=update_danhmuc).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Xóa", width=10, command=delete_danhmuc).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Tải lại", width=10, command=load_data).grid(row=0, column=3, padx=5)

# Bảng hiển thị danh mục
columns = ("ID", "Tên danh mục", "Mô tả")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=200 if col != "ID" else 50)
tree.pack(pady=10)
tree.bind("<ButtonRelease-1>", on_select)

# Tải dữ liệu khi khởi động
load_data()

root.mainloop()
