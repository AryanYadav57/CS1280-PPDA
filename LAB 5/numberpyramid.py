rows = int(input("Enter the number of rows:"))

#generate the pyramid
for i in range(1, rows+1):
	print(" "*(rows - i)+" ".join(str(num) for num in range(1, i+1)))
