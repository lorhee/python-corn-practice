import math

price_dozen_corn = 10
price_half_dozen = 5.5
price_one_corn = 1
corn_count = int(input ("Please enter quantity of corn: "))

dozen_corn = 0
half_dozen_corn = 0
single_corn = 0
if (corn_count >= 12):
    dozen_corn = math.floor(corn_count/12)
    print (dozen_corn)

if ((corn_count % 12) != 0):
    half_dozen_corn = math.floor((corn_count - dozen_corn*12)/6)
    print(half_dozen_corn)
#elif((countofcorn%6)!=0):
#else:
    single_corn = (corn_count - (dozen_corn*12) - (half_dozen_corn*6))
    print(single_corn)

corn_cost = dozen_corn * price_dozen_corn + half_dozen_corn * price_half_dozen + single_corn * price_one_corn
print ("Quantity of corn purchased =", corn_count)
print ("Cost of corn = $", corn_cost)