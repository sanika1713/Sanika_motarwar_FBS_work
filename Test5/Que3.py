Data = [[101,'seema',45000],[340,'Rajani',13000],[210,'Tanu',1400],[320,'Suresh',35000]]

# print (Data[0][2])

for ele in Data:
    # print(ele[2])
    if(ele[2]< (ele + 1)[2]):
        ele,(ele +1) = (ele + 1),ele