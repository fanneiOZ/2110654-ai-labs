"""
24 - Games
Sample initial state:
 - result: 0
 - answer: ''
 - env: [3,4,5,6]
 - b <-- branching factor
 - d <-- level
 - m <-- max depth

Final state:
 - result: 0
 - answer: '5-4+3x6'
 - env: []

Operations:
 1. add
 2. subtract
 3. multiply
 4. divide

Goal state decision:
 - env is empty
 - result === 24
"""


def add(state: tuple):
    
    return


def subtract(state: tuple):
    return


def generate_state(result: int, env: list, answer: str) -> tuple:
    return tuple([result, env, answer])


def solve_24_game(env: list):
    """
    env: list of 4 elements of digit
        - create initial state -> (0, env, answer)
        - fringe
            -> BFS = queue ~ use deque
            -> DFS = stack ~ use deque
        - push initial state -> fringe
        - pick first element
        - generate by operation <- ??
        - check breed if expected state found exit with result
        - store breed into fringe
    """
    return
