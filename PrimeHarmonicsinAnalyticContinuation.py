import tensorflow as tf
import numpy as np
from scipy import optimize

def relu(x):
    return np.maximum(x, 0)

def generate_primes(n):
    primes = []
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, p):
                sieve[i] = False
    return primes

def prime_distribution(x, w1, b1, w2, b2):
    x = np.array(x)
    x = np.expand_dims(x, axis=0)
    hidden_layer = relu(np.dot(x, w1) + b1)
    output_layer = np.dot(hidden_layer, w2) + b2
    return output_layer[0][0]

def mutate_distribution(prime_distribution_func):
    w1, b1, w2, b2 = tf.keras.backend.get_session().run(prime_distribution_func.trainable_weights)
    w1 += np.random.normal(0, 0.1, w1.shape)
    b1 += np.random.normal(0, 0.1, b1.shape)
    w2 += np.random.normal(0, 0.1, w2.shape)
    b2 += np.random.normal(0, 0.1, b2.shape)
    prime_distribution_func.set_weights([w1, b1, w2, b2])

def run_program():
    primes = generate_primes(1000)
    x = np.arange(1, 1001)
    y = np.array([optimize.newton(lambda x: prime_distribution(x, *prime_distribution_func.trainable_weights), p) for p in primes])
    prime_distribution_func = tf.keras.Sequential([
        tf.keras.layers.Dense(32, input_shape=(1,), activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    prime_distribution_func.compile(optimizer=tf.keras.optimizers.Adam(0.01), loss='mse')
    for i in range(10):
        prime_distribution_func.fit(primes, y, epochs=100, verbose=0)
        mutate_distribution(prime_distribution_func)
        print("Epoch", i+1, "- Loss:", prime_distribution_func.evaluate(primes, y))
    predictions = prime_distribution_func.predict(x)
    return x, predictions

if __name__ == "__main__":
    x, y = run_program()
    print(x, y)
