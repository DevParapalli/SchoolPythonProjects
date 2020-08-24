list_to_sum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def ListSum(list_obj):
    if len(list_obj) == 0:
        return 0
    elif len(list_obj) == 1:
        return list_obj[0]
    else:
        return list_obj[0] + ListSum(list_obj[1:])

# list_obj[1:] gives the list without the first element. 
# for next iteration we remove the second element

print(ListSum(list_to_sum))