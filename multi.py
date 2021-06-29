import sys

n = len(sys.argv)
print("Total arguments passed:", n)

print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")
for i in range(1, n):
	print(sys.argv[i], end = " ")
	
multi = 0
for i in range(1, n):
	multi *= int(sys.argv[i])
	
print("\n\nResult:", multi)
