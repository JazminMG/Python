def fibo_1(max):
	a,b=0,1
	
	while a<max:
		print(a)
		a,b=b,a+b
def fibo_2(max):
	serie = []
	a, b = 0, 1
	
	while a < max:
		serie.append (a)
		a, b = b, a+b
	return serie
	
fibo_1(10)		
print (fibo_2(10))