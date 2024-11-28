import numpy as np
sales_data = np.array([
    [100, 150, 200, 250, 300, 350], 
    [120, 160, 220, 270, 320, 370],  
    [130, 180, 230, 280, 330, 380],  
    [140, 190, 240, 290, 340, 390],  
    [150, 200, 250, 300, 350, 400]   
])
first_three_products = sales_data[:3]
print("Sales data for the first three products:")
print(first_three_products)
last_two_months = sales_data[:, -2:]
print("\nSales data for all products in the last two months:")
print(last_two_months)
specific_product_month = sales_data[1, 3]  
print("\nSales data for the 2nd product in the 4th month:")
print(specific_product_month)
print()