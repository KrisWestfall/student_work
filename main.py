def bubble_list(list_a):
    sorted = False
    indexing_length = len(list_a)-1
    
    while sorted == False:
        sorted = True
        for i in range (0, indexing_length):
            if list_a[i] > list_a[i+1]:
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
                sorted = False
    return list_a
    
print(bubble_list([1,4,2,7,4,5,8,3]))

