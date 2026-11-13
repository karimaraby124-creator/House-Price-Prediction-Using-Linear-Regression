
import pandas as pd
import numpy as np
import matplotlib as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error , r2_score

import pandas as pd

data = {
    "Area": [80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270],
    "Bedrooms": [2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5],
    "Age": [15, 10, 8, 5, 4, 3, 2, 1, 2, 1, 12, 9, 7, 6, 5, 3, 2, 2, 1, 1],
    "Garage": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    "Price": [
        450000, 550000, 650000, 750000, 850000, 950000, 1050000, 1150000, 1250000, 1350000,
        500000, 600000, 680000, 800000, 880000, 1000000, 1100000, 1200000, 1300000, 1400000
    ]
}

df = pd.DataFrame(data)

x = df[['Area' , 'Bedrooms' , 'Garage']]
y = df['Price']

x_train , x_test , y_train ,y_test = train_test_split(
    x,
    y,
    test_size= 0.2,
    random_state= 42 
)
model = LinearRegression()

model.fit(x_train , y_train)

prodect = model.predict(x_test)

mse = mean_squared_error(y_test , prodect )
r2 = r2_score(y_test , prodect)

print("mse = " , mse)
print("r2 = " , r2)

print('='*50)
new_data =  pd.DataFrame({
    "Area": [175, 120, 300],
    "Bedrooms": [4, 3, 5],
    #"Age": [3, 10, 1],
    "Garage": [1, 0, 1]
})


prodect2 = model.predict(new_data)
new_data['price ']=prodect2
print(new_data) 


print('='*40) # جزء الاختبار لصحه العمل 

test_houses = pd.DataFrame({
    "Area": [100, 130, 150, 170, 190, 210, 230, 140, 180, 250],
    "Bedrooms": [2, 3, 3, 3, 4, 4, 5, 3, 4, 5],
    "Garage": [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    "Actual Price": [
        520000,
        670000,
        780000,
        890000,
        990000,
        1100000,
        1210000,
        710000,
        920000,
        1320000
    ]
})

new_test_house = pd.DataFrame({
    "Area": [100, 130, 150, 170, 190, 210, 230, 140, 180, 250],
    "Bedrooms": [2, 3, 3, 3, 4, 4, 5, 3, 4, 5],
    "Garage": [0, 1, 1, 1, 1, 1, 1, 0, 0, 1],
    

})

prodect3 = model.predict(new_test_house)
new_test_house["new_test_house_price"] = prodect3
print(new_test_house)

mse2 = mean_squared_error(test_houses['Actual Price'] , new_test_house["new_test_house_price"])
rmse2 = np.sqrt(mse2)
print("rmse =" , rmse2)
r2_test3 = r2_score(test_houses['Actual Price'] , new_test_house["new_test_house_price"])
print("r2_tast3 =" , r2_test3)

print("mse2 = " , mse2)

print('=' * 40)
new_test_house["Actual Price"] = test_houses["Actual Price"]

new_test_house["Difference"] = (
    new_test_house["Actual Price"] -
    new_test_house["new_test_house_price"]
)

print(new_test_house)