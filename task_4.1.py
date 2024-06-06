import math

def approx_sin(x, n):
    sin_x = 0
    for k in range(n + 1):
        a = ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
        sin_x += a 
    return sin_x

def main():
    try:
        x = float(input("Nhập giá trị x: "))
        n = int(input("Nhập số lần lặp n: "))
        
        if n < 0:
            print("Số lần lặp phải là số nguyên dương")
            return

        res = approx_sin(x, n)
        print(f"Giá trị xấp xỉ của sin({x}) với {n} lần lặp là: {res}")
    except ValueError:
        print("Giá trị đầu vào không hợp lệ, vui lòng nhập số.")

main()

