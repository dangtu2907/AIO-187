import math

def approx_cosh(x, n):
    cosh_x = 0
    for k in range(n + 1):
        a = (x ** (2 * k)) / math.factorial(2 * k)
        cosh_x += a 
    return cosh_x

def main():
    try:
        x = float(input("Nhập giá trị x: "))
        n = int(input("Nhập số lần lặp n: "))
        
        if n < 0:
            print("Số lần lặp phải là số nguyên dương")
            return

        result = approx_cosh(x, n)
        print(f"Giá trị xấp xỉ của cosh({x}) với {n} lần lặp là: {result}")
    except ValueError:
        print("Giá trị đầu vào không hợp lệ, vui lòng nhập số.")

main()

