def count(s, c) :
	
	res = 0
	
	for i in range(len(s)) :
		
		if (s[i] == c):
			res = res + 1
	return res
	
S1= input("")
string = input("")
c = string[-1]
print(count(S1, c))
