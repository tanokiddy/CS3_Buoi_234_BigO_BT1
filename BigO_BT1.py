# i = 0
# while i < n:
#     i = i + 1


#1: Phân tích
    #1: Đối với vòng lặp:
        # while i < n: n lần
        # i = i + 1: 2n lần
        # Input càng lớn thì số lần lặp càng nhiều, với vòng lặp while trên thì số lần lặp là n
        # Ví dụ: n = 10, số lần lặp là 10 lần, với i chạy từ 0 - 9 (i = 10 sẽ dừng và không chạy nữa do không thoả mãn điều kiện của vòng lặp while)
    #2: Đối với đệ quy:
        # Đệ quy bản chất là 1 hàm gọi lại chính nó bên trong hàm đó
        # Điều kiện dừng trong đệ quy dùng để thoát vòng lặp, nếu không có điều kiện dừng đệ quy thì nó sẽ lặp vô tận
        
    #3: Đối với thao tác khác:
        # i = 0: 1 lần (i nằm ngoài vòng lặp)
        # while i < n: n lần
        # i = i + 1: 2n lần (2 phép toán)
#2: Output
    # F(n) = 1 + n + 2n (1 + 3n)
    # O(n)