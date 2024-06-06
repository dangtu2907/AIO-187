import math

def approx_cos(x, n):
    cos_x = 0
    for k in range(n + 1):
        a = ((-1) ** k) * (x ** (2 * k)) / math.factorial(2 * k)
        cos_x += a 
    return cos_x

def main():
    try:
        x = float(input("Nhập giá trị x: "))
        n = int(input("Nhập số lần lặp n: "))
        
        if n < 0:
            print("Số lần lặp phải là số nguyên dương")
            return

        result = approx_cos(x, n)
        print(f"Giá trị xấp xỉ của cos({x}) với {n} lần lặp là: {result}")
    except ValueError:
        print("Giá trị đầu vào không hợp lệ, vui lòng nhập số.")

main()
