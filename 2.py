Y=input() 
X=Y.split() 
Y=list(Y) 
First=X[0][0]
Second = X[1][1]
Count=0
for i in Y:
    if(i==First or i==Second) :
        Count=Count+1

print(Count)