def MD_nRE(y, y_hat, n, p):
    if len(y) != len(y_hat):
        raise ValueError("Độ dài của y và y_hat phải bằng nhau")
    
    m = len(y)
    total_error = 0
    
    for yi, y_hati in zip(y, y_hat):
        can_yi = yi ** (1/n)
        can_y_hati = y_hati ** (1/n)
        error = abs(can_yi - can_y_hati) ** p
        total_error += error
    
    md_nre = total_error / m
    return md_nre

def input_list(prompt):
    return list(map(float, input(prompt).split()))

y = input_list("Nhập danh sách các giá trị thực tế y: ")
y_hat = input_list("Nhập danh sách các giá trị dự đoán y_hat: ")
n = int(input("Nhập bậc của căn n: "))
p = int(input("Nhập p: "))
result = MD_nRE(y, y_hat, n, p)
print("MD_nRE:", result)
