import random
import matplotlib.pyplot as mtpy
def xy():
    xry = random.randint(0,1)
    if xry == 0 :
        return "X"
    else:
        return "Y" 
def pro(a):
    score = {"X" : 0, "Y" : 0}
    for k in range(a):
        score[xy()]+=1
    print("X or Y > Score :")
    print("X Score :", score["X"])
    print("Y Score :", score["Y"])

    print("\nPROBEBLITY CHECK :")
    print("'X' Probeblity :", score["X"]/a)
    print("'Y' Probeblity :", score["Y"]/a)
    # Create Plot
    mtpy.barh(score.keys(), score.values(), color=["#B700FF", "#14EEDC"])
    mtpy.show()
pro(23)



def clr():
    rbgi = random.randint(0,3)
    if rbgi==0:
        return "Red"
    elif rbgi==1:
        return "Blue"
    elif rbgi==2:
        return "Green"
    else:
        return "Purple" 
def Prb(b):
    win = {"Red":0, "Blue":0, "Green":0, "Purple":0}
    for x in range(b):
        win[clr()]+=1
    print("\n\nCOLOR's SCORE :")
    print("Red's Score    :", win["Red"])
    print("Blue's Score   :", win["Blue"])
    print("Green's Score  :", win["Green"])
    print("Purple's Score :", win["Purple"])
    print("\nPROBEBLITY CHECK :")
    print("Red's prob    :", win["Red"]/b)
    print("Blue's prob   :", win["Blue"]/b)
    print("Green's prob  :", win["Green"]/b)
    print("Purple's prob :", win["Purple"]/b)
    # Create Plot
    mtpy.bar(win.keys(), win.values(), color=["Red", "Blue", "Green", "Purple"])
    mtpy.show()
Prb(23)



import pandas as pan

student = pan.read_csv("San's  DataScience Folder\ds csv files\\student dataset_new.csv")

count = student["gender"].count()
st_gend = student.gender
gender_count = {"M" : 0, "F" : 0}

for x in st_gend:
    if (x == "M"):
        gender_count["M"]+=1
    else:
        gender_count["F"]+=1

print("\n\nGENDER COUNT :")
print("Male   :", gender_count["M"])
print("Female :", gender_count["F"])

print("\nPROBEBLITY CHECK : :")
print("Male   :", gender_count["M"]/count)
print("Female :", gender_count["F"]/count)

Key = gender_count.keys()
Value = gender_count.values()
mtpy.barh(Key, Value, color=["#5D5BE0", "#8B0981"])
mtpy.title("Student Dataset")
mtpy.show()



