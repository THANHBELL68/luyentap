import json

FILE_NAME = "products.json"


# 1. Load dữ liệu
def load_data():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# 2. Lưu dữ liệu
def save_data(products):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


# 3. Tạo ID tự động
def generate_id(products):
    return f"LT{len(products) + 1:02}"


# 4. Thêm sản phẩm
def add_product(products):
    name = input("Nhập tên sản phẩm: ")
    brand = input("Nhập thương hiệu: ")
    price = int(input("Nhập giá: "))
    quantity = int(input("Nhập số lượng: "))

    new_product = {
        "id": generate_id(products),
        "name": name,
        "brand": brand,
        "price": price,
        "quantity": quantity
    }

    products.append(new_product)
    print("✔ Thêm sản phẩm thành công!")
    return products


# 5. Cập nhật sản phẩm
def update_product(products):
    product_id = input("Nhập ID sản phẩm cần cập nhật: ")

    for product in products:
        if product["id"] == product_id:
            product["name"] = input("Tên mới: ")
            product["brand"] = input("Thương hiệu mới: ")
            product["price"] = int(input("Giá mới: "))
            product["quantity"] = int(input("Số lượng mới: "))
            print("✔ Cập nhật thành công!")
            return products

    print(" Không tìm thấy sản phẩm!")
    return products


# 6. Xóa sản phẩm
def delete_product(products):
    product_id = input("Nhập ID sản phẩm cần xóa: ")

    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            print("✔ Đã xóa sản phẩm!")
            return products

    print(" Không tìm thấy sản phẩm!")
    return products


# 7. Tìm kiếm theo tên (không phân biệt hoa thường)
def search_product_by_name(products):
    keyword = input("Nhập từ khóa tìm kiếm: ").lower()

    found = False
    for product in products:
        if keyword in product["name"].lower():
            print(product)
            found = True

    if not found:
        print("Không tìm thấy sản phẩm.")


# 8. Hiển thị tất cả
def display_all_products(products):
    if not products:
        print("Kho hàng trống.")
        return

    print("\n===== DANH SÁCH SẢN PHẨM =====")
    for product in products:
        print(f"ID: {product['id']}")
        print(f"Tên: {product['name']}")
        print(f"Thương hiệu: {product['brand']}")
        print(f"Giá: {product['price']}")
        print(f"Số lượng: {product['quantity']}")
        print("--------------------------")