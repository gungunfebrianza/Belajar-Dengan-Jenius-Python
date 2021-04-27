import sys

print(sys.argv)

for i in range(len(sys.argv)):
    if i == 0:
        print("Function name: ", sys.argv[0])
    else:
        print(f"{i:1d}. Argument: {sys.argv[i]}")

print("Coming through stdout")

# stdout is saved
save_stdout = sys.stdout

fh = open("test.txt","w")

sys.stdout = fh
print("This line goes to test.txt")

# return to normal:
sys.stdout = save_stdout

fh.close()