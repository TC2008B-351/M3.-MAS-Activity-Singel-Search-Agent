# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def check_key_in_dict(dictionary, key):
    if key in dictionary:
        return True
    return False

def search_value_in_dict(dictionary, target_value):
    for _, value in dictionary.items():
        if value == target_value:
            return True
    return False

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    """
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    stack = util.Stack()
    stack.push( start )
    visited =[]
    parentMap = {}
    actionMap = {}
    parentMap[start] = None
    actionMap[start] = None

    if problem.isGoalState(start):
            return []

    while not stack.isEmpty():
        parent = stack.pop()

        if parent in visited: continue

        if problem.isGoalState(parent):
            path = []

            current = parent
            while parentMap[current] != None:
                path.append(actionMap[current])
                current = parentMap[current]

            return path[::-1]

        visited.append(parent)
        children = problem.getSuccessors(parent)
        for child in children:
            successor, action, _ = child
            if successor not in visited:
                stack.push(successor)
                parentMap[successor] = parent
                actionMap[successor] = action

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    queue = util.Queue()
    queue.push( start )
    visited =[]
    parentMap = {}
    actionMap = {}
    parentMap[start] = None
    actionMap[start] = None

    if problem.isGoalState(start):
            return []

    while not queue.isEmpty():
        parent = queue.pop()


        if parent in visited: continue

        if problem.isGoalState(parent):
            path = []
            current = parent
            while parentMap[current] != None:
                path.append(actionMap[current])
                current = parentMap[current]

            return path[::-1]

        visited.append(parent)
        children = problem.getSuccessors(parent)
        for child in children:
            successor, action, _ = child
            if successor not in visited and successor not in queue.list:
                queue.push(successor)
                parentMap[successor] = parent
                actionMap[successor] = action

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    pqueue = util.PriorityQueue()
    visited = []
    costs = util.Counter()
    costs[start] = 0
    pqueue.push(start, costs[start])
    parentMap = {}
    actionMap = {}
    parentMap[start] = None
    actionMap[start] = None

    if problem.isGoalState(start):
            return []

    while not pqueue.isEmpty():
        parent = pqueue.pop()

        if parent in visited: continue

        if problem.isGoalState(parent):
            path = []
            current = parent
            while parentMap[current] != None:
                path.append(actionMap[current])
                current = parentMap[current]

            return path[::-1]

        visited.append(parent)
        children = problem.getSuccessors(parent)
        for child in children:
            successor, action, stepCost = child
            if successor not in visited:
                new_cost = stepCost + costs[parent]
                if successor not in costs or new_cost < costs[successor]:
                    costs[successor] = new_cost
                    pqueue.push(successor, new_cost)
                    parentMap[successor] = parent
                    actionMap[successor] = action

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    start = problem.getStartState()
    pqueue = util.PriorityQueue()
    visited = []
    costs = util.Counter()
    costs[start] = 0 + heuristic(start, problem)
    pqueue.push(start, costs[start])
    parentMap = {}
    actionMap = {}
    parentMap[start] = None
    actionMap[start] = None

    if problem.isGoalState(start):
            return []

    while not pqueue.isEmpty():
        parent = pqueue.pop()

        if parent in visited: continue

        if problem.isGoalState(parent):
            path = []

            current = parent
            while parentMap[current] != None:
                path.append(actionMap[current])
                current = parentMap[current]

            return path[::-1]

        visited.append(parent)
        children = problem.getSuccessors(parent)
        for child in children:
            successor, action, stepCost = child
            if successor not in visited:
                new_cost = stepCost + costs[parent] - heuristic(parent, problem) + heuristic(successor, problem)
                if successor not in costs or new_cost < costs[successor]:
                    costs[successor] = new_cost
                    pqueue.push(successor, new_cost)
                    parentMap[successor] = parent
                    actionMap[successor] = action

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
