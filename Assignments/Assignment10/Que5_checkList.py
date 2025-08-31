def linearSearch(li , searchEle):
    count = 0
    for ind in range(len(li)):
        if(li[ind] == searchEle):
            # count = count + 1
            return ind
        # print(count)
        
    else:
        return -1
        

li = [12, 35, 7, 84, 53,7]
searchEle = int(input("Enter the element to search:"))
res = linearSearch(li , searchEle)
if(res != -1):
    print(f'{searchEle} is found at index {res}.')
else:
    print(f'{searchEle} is not found in list.')
