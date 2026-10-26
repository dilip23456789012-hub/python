import pandas as pd

name=input("enter your Name:")

mark=[]
for i in range(5):

 marks=int(input(f"enter your marks{i+1}:"))
 mark.append(marks)

data={"name":[name],
      "mark1":[mark[0]],
       "mark2":[mark[1]],
        "mark3":[mark[2]],
         "mark4":[mark[3]],
         "mark5":[mark[4]]}

df=pd.DataFrame(data)

print(df) 
print(df.info())
print(df.describe())

