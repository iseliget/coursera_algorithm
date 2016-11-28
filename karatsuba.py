def karatsuba(x,y):
	if x < 10 or y < 10:
		return x*y
	else:
		x_right = x % (10**(len(str(x))//2))
		x_left = (x - x_right)//(10**len(str(x_right)))

		y_right = y % (10**(len(str(y))//2))
		y_left = (y - y_right)//(10**len(str(y_right)))

		u = karatsuba(x_left,y_left)
		v = karatsuba(x_right, y_right)
		w = karatsuba(x_left + x_right, y_left + y_right)
		z = w - u - v

		result = (10**(len(str(x_right))*2)) * u + (10**(len(str(y_right)))) * z + v

		return result

print(karatsuba(7345238123432176,7321234321343876))
