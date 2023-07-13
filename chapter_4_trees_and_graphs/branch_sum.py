import math
def branch_sum(arr) -> str:
    num_levels = int(math.log(len(arr),2))
    left_branch_elems = []
    right_branch_elems = []
    print(num_levels)
    for level in range(1,num_levels+1):
        start_index = int(math.pow(2,level)-1)
        num_elem_in_level = int(math.pow(2,level))
        # get the left branch
        half_num_elems = num_elem_in_level//2
        mid_index_start = start_index+half_num_elems
        for elem in arr[start_index:mid_index_start]:
            if elem != -1:
                left_branch_elems.append(elem)
        # get the right branch
        for elem in arr[mid_index_start:mid_index_start+half_num_elems]:
            if elem != -1:
                right_branch_elems.append(elem)

    left_sum = 0
    right_sum = 0

    for item in left_branch_elems:
        left_sum += item
    for item in right_branch_elems:
        right_sum += item

    if left_sum >= right_sum:
        return "left"
    else:
        return "right"

print(branch_sum([3,6,2,9,-1,10]))
print(branch_sum([3,6,2,-1,9,10]))
print(branch_sum([3,6,2,-1,9,-1, 20]))




