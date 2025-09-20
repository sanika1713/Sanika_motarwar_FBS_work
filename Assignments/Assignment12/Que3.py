def anagram(str1,str2):
    if(len(str1) != len(str2)):
        return False
    
    freq1 = {}
    freq2 = {}

    for ch in str1:
        if ch in freq1:
            freq1[ch] +=1
        else:
            freq1[ch] = 1

    for ch in str2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
        
    return True

str1 = "silent"
str2 = "listen"

if anagram(str1, str2):
    print("Anagrams")
else:
    print("Not Anagrams")