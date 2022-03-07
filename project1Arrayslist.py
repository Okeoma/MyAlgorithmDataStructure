numDays = int(input("How many day's temperature?"))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " + str(i+1)+ "'s high temp:"))
    temp.append(nextDay)
    total +=temp[i]

avg = round(total/numDays,2)
print("\nAverage = " + str(avg))

above = 0
aboveAvg =[]
for i in range(len(temp)):
    if temp[i] > avg:
        above +=1
        val = temp[i]
        aboveAvg.append(val)

print(str(above) + " day(s) temperature is above average")
print("The temperature(s) that are above average are:\n" + str(aboveAvg))
count = 0
for i in aboveAvg:
    count +=1
    print("No. " + str(count) + " temperature greater than average is :" + str(i))
