a={1,2}
b={3,4}
if a.isdisjoint(b):
    print("no common elements")
else:
    print(f"common elements are there and are:{a&b}")