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
import copy

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
    # Saida (para tinyMaze) deve ser:
    # return ['South', 'South', 'West', 'South', 'West', 'West', 'South', 'West']
    # ou seja:
    # return [(5,4), (5,3), (4,3), (4,2), (3,2), (2,2), (1,2), (1,1)]

    caminho = []
    borda = util.Stack()
    estado = problem.getStartState()
    visitados = []

    borda.push((estado,[]))
    visitados.append(estado)

    if problem.isGoalState(estado):
        estadoAtual,caminho = borda.pop()
        #print caminho
        return caminho

    while not borda.isEmpty():
        estadoAtual,caminho = borda.pop()

        if problem.isGoalState(estadoAtual):
           print "Achou o objetivo"
           #print caminho
           return caminho

        visitados.append(estadoAtual)
        # print "Estado atual: "
        # print estadoAtual
        # print caminho

        # print "Visitados:"
        # print visitados

        for s in problem.getSuccessors(estadoAtual):
            if s[0] not in visitados:
                # print "Filhos:"
                # print s[0]
                visitados.append(s[0])
                borda.push((s[0],caminho+[s[1]]))


                # print "Borda: "
                # print borda.list


    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    caminho = []
    borda = util.Queue()
    estado = problem.getStartState()
    visitados = []

    borda.push((estado,[]))
    visitados.append(estado)

    if problem.isGoalState(estado):
        estadoAtual,caminho = borda.pop()
        #print caminho
        return caminho

    while not borda.isEmpty():
        estadoAtual,caminho = borda.pop()

        if problem.isGoalState(estadoAtual):
           print "Achou o objetivo"
           #print caminho
           return caminho

        visitados.append(estadoAtual)
        # print "Estado atual: "
        # print estadoAtual
        # print caminho

        # print "Visitados:"
        # print visitados

        for s in problem.getSuccessors(estadoAtual):
            if s[0] not in visitados:
                # print "Filhos:"
                # print s[0]
                visitados.append(s[0])
                borda.push((s[0],caminho+[s[1]]))


                # print "Borda: "
                # print borda.list


    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    caminho = []
    borda = util.PriorityQueue()
    estado = problem.getStartState()
    visitados = []

    borda.push((estado,[],0),0)
    visitados.append(estado)

    if problem.isGoalState(estado):
        estadoAtual,caminho = borda.pop()
        #print caminho
        return caminho

    while not borda.isEmpty():
        estadoAtual,caminho, custo = borda.pop()

        if problem.isGoalState(estadoAtual):
           print "Achou o objetivo"
           #print caminho
           return caminho

        visitados.append(estadoAtual)
        # print "Estado atual: "
        # print estadoAtual
        # print caminho

        # print "Visitados:"
        # print visitados

        for s in problem.getSuccessors(estadoAtual):
            if s[0] not in visitados:
                # print "Filhos:"
                # print s[0]
                custo = custo + s[2]
                visitados.append(s[0])
                borda.push((s[0],caminho+[s[1]],custo),custo)


                # print "Borda: "
                # print borda.list


    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
