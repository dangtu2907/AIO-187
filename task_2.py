def is_number(x):
    try:
        float(x)
        print("True")
    except ValueError as e:
        print(e) 
        print("False")

import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha=0.01):
    if x > 0:
        return x
    else:
        return alpha * (math.exp(x) - 1)

def main():
    x = input("Nhập giá trị x = ")
    activation_function = input("Nhập tên activation function (sigmoid, relu, elu): ").strip().lower()
        
    if not is_number(x):
        print('x must be a number')
        return
    
    x = float(x)

    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f"{activation_function} function is not supported")
        return
    
    if activation_function == 'sigmoid':
        res = sigmoid(x)
    elif activation_function == 'relu':
        res = relu(x)
    elif activation_function == 'elu':
        res = elu(x)
    
    print(f"{activation_function}: f({x})={res}")

main()
