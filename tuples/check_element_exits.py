t=(5,6,7)
n=int(input("enter number for checking:"))
found=False
for i in t:
    if i == n:
        found=True
if found:
    print("element found")
else:
    print("element not found")