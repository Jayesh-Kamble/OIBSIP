print("\n-------------This Program calculate the BODY MASS INDEX (BMI) of the Individual----------------\n")
name = input("Enter your Name :")
weight = float(input("Enter your weight in Kg :"))
height = float(input("Enter your Height in centemeter :"))

height = height/100

bmi = weight /(height * height)

print(f"Your Body Mass Index is :{bmi}")

if bmi>0:
    if bmi <= 16:
        print(f"{name} you are Severely Underweight")
    elif bmi <= 18.5:
        print(f"{name} you are  Underweight...!")
    elif bmi <= 25 :
        print(f"Congratulation {name} You are Healthy person...!")    
    elif bmi <=30:
        print(f"{name} You are  Overweight")    
    else:
        print(f"{name} You are Severely Overweight....!")
else:
    print(f"Enter The Valid Details.....")        
    