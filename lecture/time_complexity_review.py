# review Big O
# most important to look at the n variable
# n is the input size variable that affects the number of steps
# constant O(1) or O(c)
# logarithmic (better than linear): O(log(n))
# linear O(n)
# polynomial O(n^2) polynomial is the 2 or (square)
# exponential O(2^n) - the more n increases, the size will explode astronomically
# factorial O(n!)
# the last three are when you look for permutations, combinations.  You only get exponential with recursion

# runs o(1)  CONSTANT TIME
def print_num(n):
    print(n)

# CONSTANT TIME O(10000)


def print_num_10000(n):
    for _ in range(10000):
        print(n)

# Linear Times
# n = 10, n will be printed 10 times
# n = 100000000 n will be printed 100000000
# relationship between input and time it takes to run the function


def print_numb_n_times(n):
    for _ in range(n):
        print(n)  # O(1)

# O(n*10000)  or O(n)  #realistically, the constant matters


def print_numb_n_times_again(n):
    for _ in range(n):  # loop runs O(n) times
        print(n)  # O(1)
        for _ in range(10000):  # O(10000)
            print(n)


# polynomial and log functions
animals = ['Duck', "jackal", "Hippo", "Aardvark", "cat",
           "Flamingo", "iguana", "Giraffe", "Elephant", "bear", "dog"]

# both rely on the length of input, being length of animals
# O(n*n) This is polynomial time
# adding another for loop would be O(n*n*n) cubic function


def print_animal_pairs():
    for animal_1 in animals:  # O(n)
        for animal_2 in animals:  # O(n)
            print(f"{animal_1} and {animal_2}")

# print_animal_pairs()


# Logarithmic Time
# we are removing HALF of the remaining animals each time
# the input gets reduced by a factor each iteration
def free_animals(animals):
    while len(animals) > 0:
        animals = animals[0: len(animals) // 2]
