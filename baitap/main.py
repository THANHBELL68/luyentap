from product_manager import *

def main():
    products = load_data()

    while True:
        print("\n===== POLY LAP MANAGEMENT =====")
        print("1. Thêm sản phẩm")
        print("2. Cập nhật sản phẩm")
        print("3. Xóa sản phẩm")
        print("4. Tìm kiếm sản phẩm")
        print("5. Hiển thị tất cả sản phẩm")
        print("6. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            products = add_product(products)

        elif choice == "2":
            products = update_product(products)

        elif choice == "3":
            products = delete_product(products)

        elif choice == "4":
            search_product_by_name(products)

        elif choice == "5":
            display_all_products(products)

        elif choice == "6":
            save_data(products)
            print("Đã lưu dữ liệu. Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()