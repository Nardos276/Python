nums=[]
target=int(input("Enter your target number: "))
n=int(input("how many numbers in the array: "))
for i in range (n):
    nums.append(int(input("Enter the numbers: ")))

if len(nums)!= len(set(nums)):
    print("You've entered the same number more than once. choose another number.")
    exit()
found= False
for i in range (len(nums)):
    for j in range (i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print("Output: ", [nums[i], nums[j]])
            found=True
            break
    if found:
        break
    else:
        continue

if not found:
    print("No pair found that sums to the target.")

        

