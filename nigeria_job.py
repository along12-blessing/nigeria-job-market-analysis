import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

class Data:
    def read_data(self):
        self.df = pd.read_csv("Nigeria_job_market.csv")
        
    def features(self):
        x = pd.get_dummies(self.df[['Industry', 'City']])
        y = self.df['Salary']
        return x, y
    
    def train_model(self, x, y):
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state = 42)
        
        model1 = DecisionTreeRegressor( random_state= 42)
        model1.fit(x_train,y_train)
        model2 = RandomForestRegressor(n_estimators=100,random_state=42)
        model2.fit(x_train,y_train)
        
        
        prediction1= model1.predict(x_test)
        prediction2 = model2.predict(x_test)
        
        return model1, model2, prediction1, prediction2, y_test
    
    def evaluate(self,model1, model2, prediction1, prediction2,y_test):
        mae1 = mean_absolute_error(y_test,prediction1)
        mae2 = mean_absolute_error(y_test, prediction2)
        
        return mae1, mae2
    
data = Data()
data.read_data()

x, y = data.features()
model1, model2, prediction1, prediction2, y_test = data.train_model(x, y)

mae1, mae2 = data.evaluate(model1, model2, prediction1, prediction2, y_test)

print(f"Decision Tree MAE: ₦{mae1:,.2f}")
print(f"Random Forest MAE: ₦{mae2:,.2f}")

if mae1 < mae2:
    print("Decision Tree is better!")
else:
    print("Random Forest is better!")