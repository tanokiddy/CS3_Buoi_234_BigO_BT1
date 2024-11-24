# i = 0
# while i < n:
#     i = i + 1


#1: Phân tích
    #1: Đối với vòng lặp:
        # while i < n: N lần
        # i = i + 1: 2N lần
        # Input càng lớn thì số lần lặp càng nhiều, với vòng lặp while trên thì tổng số lần lặp của toàn bộ các dòng lệnh là : 1 + 3N
        # Ví dụ: n = 10, số lần lặp là: 1 + 3*10 = 31 lần thực thi
    #2: Đối với đệ quy:
        # Đệ quy bản chất là 1 hàm gọi lại chính nó bên trong hàm đó
        # Điều kiện dừng trong đệ quy dùng để thoát vòng lặp, nếu không có điều kiện dừng đệ quy thì nó sẽ lặp vô tận
        
    #3: Đối với thao tác khác:
        # i = 0: 1 lần (i nằm ngoài vòng lặp)
        # while i < n: N lần
        # i = i + 1: 2N lần (2 phép toán)
#2: Output
    # F(N) = 1 + N + 2N (1 + 3N)
    # O(N)