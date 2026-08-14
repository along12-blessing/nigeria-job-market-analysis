import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV

class Job_market:
    def __init__(self):
        self.df = None
        
    def to_store(self):
        np.random.seed(42)
        cities = ['Lagos', 'Abuja', 'Port Harcourt', 'Kano', 'Ibadan']
        industries = [ 'Tech', 'Finance', 'Oil & Gas', 'Education', 'Healthcare']
        genders = ['M', 'F']
        
        data = {
            'City' : np.random.choice(cities, 50),
            'Industry': np.random.choice(industries, 50),
            'Gender': np.random.choice(genders, 50),
            'Years_Experience' : np.random.randint(1,20,50),
            'Salary': np.random.randint(150000, 1000000, 50)
        }
        
        self.df = pd.DataFrame(data)
        return self.df

class Data:
    def __init__(self, df):
        self.df = df
    def clean_data(self):
       self.df = self.df.drop_duplicates()
       self.df['Salary'] = self.df['Salary'].fillna( self.df["Salary"].mean())
       return self.df
    
    def save_file(self, path="Nigeria_job_market.csv"):
       self.df.to_csv(path, index=False)
       return path
class Train_model:
    def __init__(self, df):
        self.df = df
    def features(self):
        x = pd.get_dummies(self.df[['Industry']])  # only Industry
        x['Years_Experience'] = self.df['Years_Experience']  # add as number
        y = self.df['Salary']
        return x, y
    
    def  train(self, x, y):
        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
        
        model = RandomForestRegressor(random_state=42)
        model.fit(x_train, y_train)
        
        predictions = model.predict(x_test)        
        return  model, x_test, y_test, predictions
    
    def evaluate(self, y_test, predictions):
        from sklearn.metrics import mean_absolute_error
        mae = mean_absolute_error(y_test, predictions)
        print(f"Mean Absolute Error: ₦{mae:,.2f}")
        
    def plot_graph(self):
        import matplotlib.pyplot as plt
    
        avg_salary = self.df.groupby('Industry')['Salary'].mean()
    
        plt.bar(avg_salary.index, avg_salary.values, color=['red', 'blue', 'green', 'purple', 'orange'])
        plt.title("Average Salary by Industry in Nigeria")
        plt.xlabel("Industry")
        plt.ylabel("Salary (₦)")
        plt.show()
              

market = Job_market()
df = market.to_store()

cleaner = Data(df)
clean_df = cleaner.clean_data()
cleaner.save_file()

model_class = Train_model(clean_df)
x, y = model_class.features()
model, x_test, y_test, predictions = model_class.train(x, y)

model_class.evaluate(y_test, predictions)

model_class.plot_graph()

print(predictions)
