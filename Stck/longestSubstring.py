def LongestSubstring(str):
    stack=[]
    for ch in str:
        if ch not in stack:
            stack.append(ch)
            count+=1
str="ashish"
LongestSubstring(str)