# lst=[1,2,3,4,5,6,7,8,9]
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==9:
#             print(lst[i],lst[j])
#             break

lst=[1,2,3,4,5,6,7,8,9]
s=9
def M1(lst,s):
    res=[]
    while lst:
        num=lst.pop()
        diff=s-num
        if diff in lst:
            res.append((diff,num))
    res.reverse()
    return res
print(M1(lst,s))
