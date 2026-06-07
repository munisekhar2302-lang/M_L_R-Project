import pandas as pd
import numpy as np
import sklearn
import pickle
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
from sklearn .linear_model import LinearRegression
from sklearn.metrics import r2_score,root_mean_squared_error
df= pd.read_csv('Student_Performance.csv')
df['Extracurricular Activities']=df['Extracurricular Activities'].map({'Yes':1,'No':2})
class MLR:
  def __init__(self,path):
    self.path=path
    self.df=self.path
    self.X=self.df.iloc[:,:-1]
    self.y=self.df.iloc[:,-1]
    self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X ,self.y,test_size=0.2,random_state=42)
  def train (self) :
    self.reg=LinearRegression()
    self.reg.fit(self.X_train,self.y_train)
    print(f'Train Accuracy is :{r2_score(self.y_train,self.reg.predict(self.X_train))}')
    print(f'Train loss is : {root_mean_squared_error(self.y_train,self.reg.predict(self.X_train))}')
  def test (self):
     print(f'Test Accuracy is : {r2_score(self.y_test, self.reg.predict(self.X_test))}')
     print(f'Test Loss is : {root_mean_squared_error(self.y_test, self.reg.predict(self.X_test))}')
  def saved_file (self):
    with open ('MLR_Model','wb')  as f:
      pickle.dump(self.reg,f)
  def load_file(self):
    with open ('MLR_Model','rb') as f:
      self.m=pickle.load(f)
  def sample(self,Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleep_Hours,Sample_Question_Papers_Practiced):
    result=self.m.predict([[Hours_Studied,Previous_Scores,Extracurricular_Activities,Sleep_Hours,Sample_Question_Papers_Practiced]])
    print(f'studet performance is :{result[0]}')
if __name__=='__main__':
  obj=MLR(df)
  obj.train()
  obj.test()
  obj.saved_file ()
  obj.load_file()
  obj.sample(10,2,1,5,2)
