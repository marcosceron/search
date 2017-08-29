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
    # reachedGoal = False
    # exploredAll = False
    #
    # startState=problem.getStartState()
    #
    # exploredStatesDictionary=util.Counter()
    # exploredStatesDictionary[0] = problem.getStartState()
    # frontierDictionary=util.Counter()
    # frontierList=problem.getSuccessors(problem.getStartState())
    # #hash table for list of vertices as key
    # vectorDictionary={}
    #
    #
    #
    # #create stack to hold the frontier states
    # frontierQueue=util.Stack()
    # #queue to hold list of actions
    # #actionsQueue=util.Queue()
    # actionsQueue=[]
    #
    #
    # #push the frontier states onto the stack
    # for i in frontierList:
    #     fNode=i
    #     frontierQueue.push(fNode)
    #
    # for i in frontierList:
    #     actionsThisFar=copy.deepcopy(actionsQueue)
    #     successor = str(i[0])
    #     vectorDictionary[successor]=actionsThisFar
    #
    #
    # #key variable, key to exploredStatesDictionary
    # seenAlready=1
    # while reachedGoal==False:
    #
    #
    #     #get next state to explore, the first state from the stack
    #     #also save the action required to get to that point
    #     tempState=frontierQueue.pop()
    #     nextState=tempState[0]
    #     nextAction=tempState[1]
    #
    #     #save the explored state
    #     exploredStatesDictionary[seenAlready] = nextState
    #     #save the action taken
    #     actionsQueue.append(nextAction)
    #
    #
    #     seenAlready = seenAlready+1
    #
    #
    #     #next state becomes current state
    #     if (exploredAll == True):
    #         inc=0
    #         otherInc=0
    #
    #
    #
    #         reset = str(tempState[0])
    #
    #         newActionsList = vectorDictionary[reset]
    #         newActionsList.append(tempState[1])
    #
    #         #empty the old action list
    #         actionsQueue=copy.deepcopy(newActionsList)
    #
    #
    #     currentState=nextState
    #
    #     #check if it is goal
    #     if (problem.isGoalState(currentState)):
    #         reachedGoal=True
    #
    #     else:
    #         #the current state is not the goal
    #         #acquire the new frontier
    #
    #
    #         frontierList=problem.getSuccessors(currentState)
    #         for i in frontierList:
    #             actionsThisFar=copy.deepcopy(actionsQueue)
    #             successor = str(i[0])
    #             vectorDictionary[successor]=actionsThisFar
    #
    #
    #         first = frontierList[0]
    #
    #         #push the unexplored frontier states onto the queue
    #
    #         explored=False
    #
    #         counter=0
    #
    #
    #
    #     for i in frontierList:
    #
    #          #counter to keep track of iterations
    #          explored=False
    #          exploredAll = False
    #          for k in exploredStatesDictionary:
    #               stateCo=exploredStatesDictionary[k]
    #
    #               if ((i[0] == stateCo)):
    #
    #                    explored = True
    #                    counter = counter+1
    #
    #               if(counter == ((len(frontierList)))):
    #                     exploredAll = True
    #
    #
    #               elif ((explored == False) and (k == ((len(exploredStatesDictionary)))-1)):
    #                     fNode = i
    #                     frontierQueue.push(fNode)
    #
    #
    #
    # print actionsQueue

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    caminho = []

    borda = util.Stack()
    estado = problem.getStartState()
    visitados = []
    borda.push(estado)
    visitados.append(estado)
    caminho.append(estado)

    if problem.isGoalState(estado):
        estadoAtual = borda.pop()
        return caminho


    while not borda.isEmpty():
        estadoAtual = borda.pop()
        proximosEstados = problem.getSuccessors(estadoAtual)
        borda.push(proximosEstados[0][0])

        if problem.isGoalState(proximosEstados[0][0]) and not proximosEstados[0][0] in visitados:
            estadoAtual = borda.pop()
            visitados.append(estadoAtual)
            caminho.append(estadoAtual)
            return caminho
        else:
            visitados.append(proximosEstados[1][0])
            borda.push(proximosEstados[1][0])
            if problem.isGoalState(proximosEstados[1][0] and not proximosEstados[1][0] in visitados):
                estadoAtual = borda.pop()
                visitados.append(estadoAtual)
                caminho.append(estadoAtual)
                print borda.list
                raise SystemExit
                return caminho


    return caminho







def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
