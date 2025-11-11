from common.updatedanhmuc import update_danhmuc

while True:
    ma=input("Nhập vào mã danh mục")
    ten=input("Nhập vào tên danh mục")
    mota=input("Nhập vào mô tả")
    update_danhmuc(ma,ten,mota)
    con = input("TIẾP TỤC y, THOÁT THÌ NHẤN KÝ TỰ BẤT KỲ")
    if con != "y":
        break