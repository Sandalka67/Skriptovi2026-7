def is_prime(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


n = int(input())
while n < 5:
    n = int(input())

twin_pairs = []

for p in range(2, n - 1):
    if is_prime(p) and is_prime(p + 2):
        twin_pairs.append((p, p + 2))
        print(p, p + 2)

print(len(twin_pairs))

if twin_pairs:
    largest_pair = twin_pairs[-1]
    print(largest_pair[0], largest_pair[1])
else:
    print("Няма")
