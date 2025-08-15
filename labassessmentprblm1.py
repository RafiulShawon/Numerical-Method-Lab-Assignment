#find the smallest number in the loop

arr=[70,56,4,5,45]
lowest=arr[0]

for x in arr:
    if x<lowest:
        lowest=x

print("Smallest number is:",lowest)        
