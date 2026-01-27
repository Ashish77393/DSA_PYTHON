def GenerateParanthesis(idx,total,brackets,result):
    if idx>=len(brackets):
        if total==0:
            result.append(''.join(brackets))
        return
    if total>len(brackets)//2 or total<0 :
        return
    brackets[idx]="("
    sum=total+1
    GenerateParanthesis(idx+1,sum,brackets,result)
    brackets[idx]=")"
    sum=total-1
    GenerateParanthesis(idx+1,sum,brackets,result)
n=2
brackets=[""]*(2*n)
result=[]
GenerateParanthesis(0,0,brackets,result)
print(result)
