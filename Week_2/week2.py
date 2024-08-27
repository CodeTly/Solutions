# dictionary to store number and its index
def findsums(nums, target):
    num_to_index = {}
    
    # iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        # check if the complement exists in the dictionary
        if complement in num_to_index:
            return (num_to_index[complement], i)
        # add the number and its index to the dictionary
        num_to_index[num] = i
    
    # return None if no solution is found
    return None

def main():
    # input the number of elements
    nums_size = int(input("Enter the number of elements: "))
    
    # input the numbers
    nums = []
    print("Enter the numbers:")
    for _ in range(nums_size):
        nums.append(int(input()))
    
    # input the target
    target = int(input("Enter the target value: "))
    
    # find the two indices
    indices = findsums(nums, target)

    #print the indices
    if indices:
        print(f"Indices: {indices[0]}, {indices[1]}")
    else:
        print("No two numbers add up to the target.")

if __name__ == "__main__":
    main()
