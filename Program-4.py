numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]

# Initialize the result dictionary
result = {i: 0 for i in range(1, 10)}

# Count multiples
for i in range(1, 10):
    for num in numbers:
        if num % i == 0:
            result[i] += 1

# Print the result
print(result)
