#Write a Python script that asks the user for their weight in kilograms and height in meters, then calculates and prints their 
#Body Mass Index (BMI).
#Formula: BMI = weight / (height ** 2)

kilograms = input('Please enter your weight in kilograms: ')
meters = input('Please enter your height in meters: ')

bmi = int(kilograms) / (float(meters) ** 2)
print('')
print ('Your Body Mass Index (BMI) is: ',bmi)