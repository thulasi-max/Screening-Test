a = int(input("Enter a: "))

for i in range(1, a + 1, 2):
    print(i, end=", " if i + 2 <= a else "\n")
