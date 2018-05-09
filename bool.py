#find highest value in the list and use index to assign 

highest = 0
index = 0

for crime in crime_rates:
    if crime > highest:
        highest = crime
    index = crime
    
print(crime_rates)
print(highest)
