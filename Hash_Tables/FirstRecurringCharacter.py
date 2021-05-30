
# Question: 
# Find the first recurring character in an array / string
# 
#
# 

# Solution 1 (Naive Solution)
# Time complexity O(n^2)
def find_first_recurring_character1(array):
    # Iterate through every element
    for i in range(0, len(array)):
        # Check all previous elements
        for j in range(0, i):
            # If any 2 entries are same recurring character found
            if i != j:
                if array[i] == array[j]:
                    return array[i]


# Solution 2 (Using Hash Tables)
# Time Complexity O(n)
# Space Complexity O(n) for storing hash table
def find_first_recurring_character2(array):
    # Hash table consisting of the occurences
    # set() is a Hash Table with only the keys
    occurences = set()
    # Iterate through every element in array
    for i in range(0, len(array)):
        # Lookup element in hash table
        # if present it is a recurring character
        # else add to table for reference
        if array[i] in occurences:
            return array[i]
        else:
            occurences.add(array[i])
    return None


array = [1,2,3,4,5,5,3,2]

print([1,2,3,4,5,5,3,2],"First Recurring Character (Naive Solution): " , find_first_recurring_character1(array))

print([1,2,3,4,5,5,3,2],"First Recurring Character (Hash Table): ", find_first_recurring_character2(array))

print(list("akshay"),"First Recurring Character (Hash Table): ", find_first_recurring_character2(list("akshay")))