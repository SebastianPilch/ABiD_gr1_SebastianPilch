
def sort_swap(lst):
    if all(isinstance(x, int) for x in lst):
        for i in range(0, len(lst)-1):
            min = lst[i]
            min_id = i
            for j in range(i + 1, len(lst)):
                if lst[j] < min:
                    min = lst[j]
                    min_id = j
            lst[min_id], lst[i] = lst[i], lst[min_id]
        return lst
    return None

l_ns = [2,6,12,9,3,7,11,4,5,10,8,1]
print(sort_swap(l_ns))