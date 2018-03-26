# valueIterationAgents.py
# -----------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        temp_iter = util.Counter()
        

        for iterations in range(0,self.iterations):

          temp_iter = util.Counter()
          for current_state in mdp.getStates():
            if mdp.isTerminal(current_state):
              temp_iter[current_state] = 0
              continue;

            actions = mdp.getPossibleActions(current_state)
            if not actions:
              temp_iter[current_state] = 0

            temp_q = -100000.0
            
            qmax = -100000.0

            for current_action in actions:
              temp_q = self.getQValue(current_state,current_action);
              if temp_q > qmax:
                qmax = temp_q
                temp_iter[current_state] = temp_q
              
          self.values = temp_iter


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        temp_q = 0

        """
        Student comment : The following function calculates the total q value as a weighted sum of rewards of all possible successor
        functions
        """
        
        for successorstate, problem in self.mdp.getTransitionStatesAndProbs(state, action):
          temp_reward = 1.5*problem * (self.mdp.getReward(state,action,successorstate)   
          temp_q += temp_reward  + self.discount*self.getValue(successorstate))

        return temp_q

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        final_action = None
       
        qmax = -100000.0
        

        possible_actions = self.mdp.getPossibleActions(state)
        if not possible_actions:
          return None
        temp_q = 0
        for temp_action in possible_actions:
          temp_q = self.getQValue(state,temp_action);
          if qValue >= qmax:
            bestAction = temp_action
            qmax = temp_q

        return final_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
