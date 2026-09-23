n = int(input("Enter n: "))

for i in range(1, n + 1):
    print("\nTable of", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)