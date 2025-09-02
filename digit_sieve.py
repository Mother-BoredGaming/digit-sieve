def ends_with_1379(n):
    return str(n)[-1] in {'1', '3', '7', '9'}

def next_valid_multiple(p, start):
    m = start + p
    while not ends_with_1379(m):
        m += p
    return m

def generate_primes(limit):
    primes = [3, 7]
    multiples = {p: next_valid_multiple(p, p) for p in primes}
    candidates = []

    while len(primes) < limit:
        # Sort multiples by value, then by prime (to prioritize smaller prime on collision)
        sorted_mults = sorted(multiples.items(), key=lambda x: (x[1], x[0]))
        low1_p, low1_m = sorted_mults[0]
        low2_p, low2_m = sorted_mults[1]

        # Find candidates between the two lowest multiples
        for n in range(low1_m + 1, low2_m):
            if ends_with_1379(n) and n not in multiples.values():
                candidates.append(n)

        # Add new primes and their first valid multiples
        for c in candidates:
            if c not in primes:
                primes.append(c)
                multiples[c] = next_valid_multiple(c, c)

        candidates.clear()

        # Advance the multiple of the smaller prime if there's a collision
        current_mults = set(multiples.values())
        new_mult = next_valid_multiple(low1_p, low1_m)
        while new_mult in current_mults:
            new_mult = next_valid_multiple(low1_p, new_mult)
        multiples[low1_p] = new_mult

    return primes

# Run the sieve and print the 2000th prime
primes = generate_primes(2000)
print(primes[-1])  # Should print 17401
