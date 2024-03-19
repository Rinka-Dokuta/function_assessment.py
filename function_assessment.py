armor = 0
product = 0
dif = 0
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
bum1 = 0
sum = 0


def calculate_health(Health, damage, armor):
    
    product = damage * armor
    dif = Health - product
   
    print("Your current health is", dif)
    
calculate_health(100, 10, .5)


def average_of_five(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    quotient = sum // 5
    
    print("The average is", quotient)
    
average_of_five(10, 20, 30, 40, 50)
    
