import numpy as np

# Define the prime harmonic function
def prime_harmonic(n):
    primes = []
    for i in range(2, n+1):
        for j in range(2, int(np.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return np.sum(np.sin(primes))

# Define the analytic continuation function
def analytic_continuation(z):
    return np.sum([1/(n**z) for n in range(1, 100)])

# Define the main function
def prime_distribution(n, z):
    # Generate the prime harmonic sequence
    prime_harmonic_seq = [prime_harmonic(i) for i in range(1, n+1)]

    # Apply the analytic continuation function to the sequence
    analytic_continuation_seq = [analytic_continuation(complex(z, p)) for p in prime_harmonic_seq]

    # Normalize the sequence
    normalized_seq = [x/np.max(analytic_continuation_seq) for x in analytic_continuation_seq]

    return normalized_seq
