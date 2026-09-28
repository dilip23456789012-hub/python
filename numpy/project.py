#guess the students exam score based on the number of hoursstudied and attendence
import numpy as np
np.random.seed(42)
studentstudy=np.random.randint(1,8,5)
studentattendence=np.random.randint(60,101,5)
previousscore=np.random.randint(40,91,5)
print("studentstudy",studentstudy)
print("studentatrendence",studentattendence)
print("previousscore",previousscore)
result=studentstudy+studentattendence+previousscore
print(result/3)

