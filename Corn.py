import math

pricedozencorn = 10
pricehalfdozen=5.5
priceonecorn = 1
countofcorn = int(input ("Please enter quantity of corn: "))

dozencorn=0
halfdozencorn=0
singlecorn=0
if (countofcorn >=12):
    dozencorn=math.floor(countofcorn/12)
    print (dozencorn)

if ((countofcorn%12)!=0):
    halfdozencorn= math.floor((countofcorn-dozencorn*12)/6)
    print(halfdozencorn)
#elif((countofcorn%6)!=0):
#else:
    singlecorn=(countofcorn-(dozencorn*12)-(halfdozencorn*6))
    print(singlecorn)


costofcorn =dozencorn*pricedozencorn+halfdozencorn*pricehalfdozen+singlecorn*priceonecorn
print ("Quantity of corn purchased =", countofcorn)
print ("Cost of corn = $", costofcorn)