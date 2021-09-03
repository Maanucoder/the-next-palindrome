#take input from user
n=input()
while True:
# a blank list for further use
		l=[]
#transform n into int
		n=int(n)
#to get succeed number from n.
		n=n+1
		for item in str(n):
#appending the item into blank list l
			l.append(item)
#make a copy of l
		z=l.copy()
#reverse l and store in r
		r=l[::-1]
#join l and r to get a string
		j1="".join(l)
		j2="".join(r)
#check j1 is equal or not to j2
		if j1==j2:
				print(j2)
				break



				
			
		
		
			
	
	
		
		
	
