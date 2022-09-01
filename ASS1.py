for i in range(1,200+1):
    if i > 1:
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            print(i)

print("")            
print("All are prime value 1 to 200 with help of for loop and range")
print("")
