def has_unique_in_range_property(A):
    last_index = {}
    
    for i in range(len(A)):
        unique_in_range = True
        
        if A[i] not in last_index:
            last_index[A[i]] = i
        else:
            if any(A[j] == A[i] and last_index[A[i]] < j < i for j in range(last_index[A[i]]+1, i)):
                return False
            else:
                last_index[A[i]] = i
    
    return unique_in_range

print(has_unique_in_range_property([1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1]))
print(has_unique_in_range_property([1, 2, 3, 4, 5, 6, 1, 2 , 3, 4, 4, 5, 6]))
print(has_unique_in_range_property([1, 2, 3, 1, 2, 3]))