# Digit-Filtered Prime Sieve

This Python script implements a nontraditional prime sieve that generates primes by exclusion rather than direct testing. It begins with 3 and 7, and only considers numbers ending in 1, 3, 7, or 9—automatically excluding multiples of 2 and 5.

## How It Works
- Starts with initial primes: 3 and 7
- Tracks their valid multiples (those ending in 1, 3, 7, or 9)
- Compares the two lowest multiples to identify gaps where new primes must lie
- Adds new primes to the pool and tracks their valid multiples
- Advances the multiple of the smaller prime when collisions occur

## Verification
Confirmed: the 2000th prime (excluding 2 and 5) is correctly identified as **17,401**.

## How to Run
Use any Python 3 environment. Run `digit_sieve.py` to generate primes. The script prints the 2000th prime by default.

## Notes
This sieve is structurally sound, digit-aware, and self-evolving. It avoids divisibility checks entirely and relies on dynamic exclusion logic. Feel free to fork, benchmark against classical sieves, or explore adaptations in other bases.

