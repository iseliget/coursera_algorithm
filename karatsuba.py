def karatsuba(x,y):
	'''
	using notations in this slide
	https://courses.csail.mit.edu/6.006/spring11/exams/notes3-karatsuba
	'''
	if x<10 or y<10:
		return x*y
	else:
		total_length = len(str(x))

		x_right = x % (10**(total_length//2))
		x_left = (x - x_right)//(10**(total_length//2))

		y_right = y % (10**(total_length//2))
		y_left = (y -y_right)//(10**(total_length//2))

		a = karatsuba(x_left,y_left)
		d = karatsuba(x_right,y_right)
		e = karatsuba(x_left+x_right,y_left+y_right) - a - d

		return a * (10**(((total_length)//2)*2)) + e * (10**(total_length//2)) + d

def test(x,y):
	if x*y == karatsuba(x,y):
		print("Correct")
	else:
		print("Incorrect: answer should be " + str(x*y) + ", output is " + str(karatsuba(x,y)))

test(1003,2749)
test(1342,2832)
test(10582,49775)
test(82097,75724)
test(29372,80583)
test(18372939,59375028)
test(10582097,49775724)
test(105820974944592,497757247093699)
test(884197169399375105820974944592,497757247093699959574966967627)
test(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
