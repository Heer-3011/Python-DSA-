# Input: hello

# Output:
#     jfus
#    flsf
#    sowe
#    hello
#    Target matched after 3 iterations

import random
import string

target = "ab"
iterations = 0

while True:
    guess = ''.join(random.choice(string.ascii_lowercase)
                    for _ in range(len(target)))

    print(guess)

    if guess == target:
        print(f"Target matched after {iterations} iterations")
        break

    iterations += 1
