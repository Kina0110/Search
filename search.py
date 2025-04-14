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

#Yakina Azza yxa220026
#Ryan Duxstad rad210000


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

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    frontier = util.Stack()
    startState = problem.getStartState()
    frontier.push((startState, []))  # (state, actions)
    
    explored = set()
    
    # While the frontier is not empty
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        
        if problem.isGoalState(state):
            return actions
            
        # Add to explored set 
        if state not in explored:
            explored.add(state)
            
            for nextState, action, cost in problem.getSuccessors(state):
                if nextState not in explored:
                    frontier.push((nextState, actions + [action]))
    
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # Initialize frontier 
    frontier = util.Queue()
    startState = problem.getStartState()
    frontier.push((startState, []))  
    
    # Initialize explored set 
    explored = set()

    explored.add(startState)
    
    # Frontier isnt empty
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        
        # When goal state is reached
        if problem.isGoalState(state):
            return actions
            
        for nextState, action, cost in problem.getSuccessors(state):
            if nextState not in explored:
                frontier.push((nextState, actions + [action]))
                explored.add(nextState) 
    
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # Initialize frontier 
    frontier = util.PriorityQueue()
    startState = problem.getStartState()
    frontier.push((startState, []), 0)  # priority=cost
    
    # Initialize explored set
    explored = set()
    
    # While the frontier is not empty
    while not frontier.isEmpty():
        state, actions = frontier.pop()
        
        if problem.isGoalState(state):
            return actions
            
        if state not in explored:
            explored.add(state)
            
            # Expand node, adding to frontier
            for nextState, action, stepCost in problem.getSuccessors(state):
                if nextState not in explored:
                    nextActions = actions + [action]
                    priority = problem.getCostOfActions(nextActions)
                    frontier.push((nextState, nextActions), priority)
    
    # Frontier empty
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    frontier = util.PriorityQueue()
    startState = problem.getStartState()
    frontier.push((startState, []), heuristic(startState, problem)) 
    
    # Initialize explored set
    explored = set()
    
    # Frontier not empty
    while not frontier.isEmpty():
        # pop from frontier
        state, actions = frontier.pop()
        
        # node is goal state
        if problem.isGoalState(state):
            return actions
            
        # if not explored, add to explored set 
        if state not in explored:
            explored.add(state)
            
            # Expand node, adding others to frontier if not there already
            for nextState, action, stepCost in problem.getSuccessors(state):
                if nextState not in explored:
                    nextActions = actions + [action]
                    g_n = problem.getCostOfActions(nextActions)  # g(n) = path cost
                    h_n = heuristic(nextState, problem)         # h(n) = heuristic estimate
                    f_n = g_n + h_n                            # f(n) = g(n) + h(n)
                    frontier.push((nextState, nextActions), f_n)
    
    # If the frontier is empty then return 
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
