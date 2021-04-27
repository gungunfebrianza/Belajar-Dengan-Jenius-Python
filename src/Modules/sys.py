import sys

print(sys.argv)

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: ", sys.argv[0])
    else:
        print(f"{i:1d}. Argument: {sys.argv[i]}")

