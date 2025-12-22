def singleNumber( nums):
    map={}
    for i in nums:
        if i  in  map:
            map[i] = map[i]+1
        else:
            map[i] = 1
    res =0
    for k,v in map.items():
        if v == 1:
            res =k        
    return res

print(singleNumber([4,1,2,1,2]))