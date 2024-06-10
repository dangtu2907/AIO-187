import random
import math

def calculate_loss(num_samples, loss_name):
    def mae(predictions, targets):
        return sum(abs(p - t) for p, t in zip(predictions, targets)) / len(predictions)
    
    def mse(predictions, targets):
        return sum((p - t) ** 2 for p, t in zip(predictions, targets)) / len(predictions)
    
    def rmse(predictions, targets):
        return math.sqrt(mse(predictions, targets))
    
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    
    num_samples = int(num_samples)
    
    loss_name = loss_name.strip().upper()  
    
    predictions = []
    targets = []
    
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        predictions.append(predict)
        targets.append(target)
        print(f"sample-{i+1}: predict = {predict:.2f}, target = {target:.2f}")

    if loss_name == 'MAE':
        loss = mae(predictions, targets)
    elif loss_name == 'MSE':
        loss = mse(predictions, targets)
    elif loss_name == 'RMSE':
        loss = rmse(predictions, targets)
    else:
        print("Invalid loss name")
        return
    
    print(f"{loss_name} loss: {loss:.4f}")

num_samples = input("Enter number of samples: ").strip() 
loss_name = input("Enter loss name (MAE, MSE, RMSE): ")

calculate_loss(num_samples, loss_name)

