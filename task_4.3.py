import math

def approx_sinh(x, n):
    sinh_x = 0
    for k in range(n + 1):
        a = (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        sinh_x += a 
    return sinh_x

def main():
    try:
        x = float(input("Nhập giá trị x: "))
        n = int(input("Nhập số lần lặp n: "))
        
        if n < 0:
            print("Số lần lặp phải là số nguyên dương")
            return

        result = approx_sinh(x, n)
        print(f"Giá trị xấp xỉ của sinh({x}) với {n} lần lặp là: {result}")
    except ValueError:
        print("Giá trị đầu vào không hợp lệ, vui lòng nhập số.")

main()


