import sys

print("Coming through stdout")

# stdout is saved
save_stdout = sys.stdout

fh = open("test.txt","w")

sys.stdout = fh
print("This line goes to test.txt")

# return to normal:
sys.stdout = save_stdout

fh.close()