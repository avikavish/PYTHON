
# searching for the element using for loop
#1,4,9,16,36,49,64,89,100]

nums = [1,4,9,16,36,49,64,89,100]    # output will be index number

x =9
idx =0
for el in nums:
    if el ==x:
        print("found",idx)
  
    idx+=1