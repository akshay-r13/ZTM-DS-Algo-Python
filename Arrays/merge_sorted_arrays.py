# Given 2 sorted arrays write a function to merge them.
# Example:
# Array1 = [1, 7, 21, 32] , Array2 = [3 , 10, 15, 30]
# Merged Array = [1, 3, 7, 10, 15, 21, 30, 32]

def merge_sorted_arrays(array1, array2):
    merged_array = []
    pointer = 0
    for i in range(0, len(array1)):
        for j in range(pointer, len(array2)):
            if array2[j] < array1[i]:
                merged_array.append(array2[j])
                pointer = j + 1
            else:
                merged_array.append(array1[i])
                break
                
    return merged_array

array1 = [1, 7, 21, 21, 32]
array2 = [3 , 10, 15, 21, 30]

print("Array 1 : ", array1)
print("Array 2 : ", array2)
print("Merged Array : ", merge_sorted_arrays( array1, array2 ))