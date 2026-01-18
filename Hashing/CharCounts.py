# 1st Mrthod
# def charCounts(s,m):
#     hash_list=[0]*26
#     for ch in s:
#         ascii_value=ord(ch)
#         index=ascii_value-97
#         hash_list[index]+=1
#     for ch in m:
#         ascii_value=ord(ch)
#         index=ascii_value-97
#         print(hash_list[index])



# Second Method
def charCounts(s, m):
    hash_list = [0] * 26
    
    for ch in s:
        if 'a' <= ch <= 'z':
            hash_list[ord(ch) - 97] += 1
    
    for ch in m:
        if 'a' <= ch <= 'z':
            print(f"{ch} -> {hash_list[ord(ch) - 97]}")
        else:
            print(f"{ch} -> Invalid character")
n="ashishkumarSingh"
m=['a','s','i',"S"]
charCounts(n,m)