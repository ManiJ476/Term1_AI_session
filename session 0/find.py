def is_subsequence(s1,s2):
    i = 0
    j = 0
    while i<len(s1) and j<len(s2):
        if(s1[i]==s2[j]):
            i+=1
        j+=1
    if(i==len(s1)):
        return 1
    else:
        return 0
    
print(is_subsequence("apple", "adcsjncjsppaxjjnaxle"))
print(is_subsequence("apple", "bsdpple"))
print(is_subsequence("apple", "paple")) 