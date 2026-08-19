import pandas as pd 
import numpy as np
data = pd.DataFrame({
    "Attendance":[ "High_attendance" , "Low_attendance" ,"TOTAL"] ,
    "PASS" : [40,25,70] ,
    "FAIL" : [5 , 25 , 30] , 
    "TOTAL" : [50,50,100] ,
  })
data = data.set_index("Attendance")
data = data / 100 
print(data)
joint_probability = data.loc["High_attendance" , "PASS" ]
marginal_probability = data.loc["TOTAL","PASS"]
print("Joint probability:", joint_probability)
print("Marginal probability:", marginal_probability)