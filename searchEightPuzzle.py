from searchProblem import Search_problem, Arc
from eightPuzzle import start, goal, count_misplaced, next_moves, move
import random
from searchMPP import SearcherMPP

class EightPuzzleGridProblem(Search_problem):
    def __init__(self, start=start):
        self.start = start
    def start_node(self):
        return self.start
    def is_goal(self, node):
        return node == goal
    def neighbors(self, node):
        return (Arc(node, move(node, next)) for next in next_moves(node))
    def heuristic(self, node):
        return count_misplaced(node, goal)
    
def shuffle(count = 1000):
    board = goal
    for i in range(count):
        moves = next_moves(board)
        next = random.randint(0, len(moves) - 1)
        board = move(board, moves[next])
    return board

def search():
    searcher = SearcherMPP(EightPuzzleGridProblem())
    searcher.search()

def searchRandom():
    searcher = SearcherMPP(EightPuzzleGridProblem(shuffle()))
    searcher.search()

def searchInput():
    board = []
    for i in range(9):
        value = input("Enter the " + str(i) + "th element: ")
        value = 0 if value == "" else int(value)
        board.append(value)
    board = tuple(board)
    print(board)
    searcher = SearcherMPP(EightPuzzleGridProblem(board))
    searcher.search()