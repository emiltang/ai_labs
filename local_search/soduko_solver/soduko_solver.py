from random import randint

INITIAL_POP_SIZE = 10
POP_SIZE = 50
CROSSOVER_RATE = 0.05
MUTATION_RATE = 0.9
MAX_STEPS = 1000000


def generate_random_state(initial_state):
    return [randint(1, 10) if j == 0 else j for j in initial_state]


def generate_initial_pop(initial_state):
    """Randomly generate n states"""
    return [generate_random_state(initial_state) for _ in range(0, INITIAL_POP_SIZE)]


def check_squares(state):
    squares_indexes = [i + j for j in range(0, 9, 3) for i in range(0, len(state), len(state) // 3)]
    squares = [state[pos + i:pos + i + 3] for pos in squares_indexes for i in range(0, 19, 9)]
    flat_list = [squares[i:i + 3] for i in range(0, len(squares), 3)]
    # s = [sum(lst) for lst]
    return 4


def rank_state(state):
    """Fitness function"""
    return check_squares(state) + check_lines(state)


def check_lines(state):
    lines = [state[pos:pos + 9] for pos in range(0, len(state), 9)]
    errors = [i for i in lines if sum(i) != 45]
    return len(errors)


def search(initial_state):
    """Genetic Search"""
    population = {}
    for s in generate_initial_pop(initial_state):
        population[rank_state(s)] = s

    for _ in range(0, MAX_STEPS):



    return 4


def main():
    # Read input
    with open('input') as f:
        ints = [int(i) for i in f.read().split()]
    result = search(ints)
    print(result)


if __name__ == "__main__":
    main()
