t1 = "HelloWorld"
text = list(t1)
for i in range(len(text)):
    if(i==0):
        text[i],text[len(text)-1] = text[len(text)-1] , text[i]
    # print(text)
result = "".join(text)
print(result)