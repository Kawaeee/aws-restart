# 18.challenge-lab.py (Kasidech C.)

def is_prime(number: int):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def main():
    with open("18.results.txt", "w") as output_file:  # Store the results in a results.txt file.
        for i in range(1, 251):
            prime_check = is_prime(i)
            if prime_check:
                output_file.write(f"{i}\n")  # Display all the prime numbers between 1 to 250.


if __name__ == "__main__":
    main()
