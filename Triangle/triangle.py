
def classTriangle(a , b, c):
	print("Input lengths of the triangle sides: ")
#	a = int(input("a: "))
#	b = int(input("b: "))
	#c = int(input("c: "))

	if a == b == c:
		print("Equilateral triangle")
	elif a==b or b==c or c==a:
		print("Isosceles triangle")
	elif (a*a+b*b == c*c) or (a*a+c*c == b*b) or (c*c+b*b == a*a):
    	print("Right angle triangle")
	else:
		print("Scalene triangle")