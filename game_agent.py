"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass

def heuristic_1(game, player):
    """
    First heuristic attempt.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float((own_moves * 2) - opp_moves)

def heuristic_2(game, player):
    """
    In this heuristic, the distance between 2 players is computed as the score.
    The hypothesis is: If two players are far from each other, it’s better than
    if they are close, as the opponent move will be less likely to occupy one of
    the legal moves from the active player.
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    player_possition = game.get_player_location(player)
    opponent_possition = game.get_player_location(game.get_opponent(player))
    return float(abs(sum(player_possition) - sum(opponent_possition)))

def heuristic_3(game, player):
    """
    In this heuristic, if a player legal moves contains corners, the number of
    corners is substracted from the number of legal moves.This, to avoid
    selecting scenarios where the player heads to a corner. Both the oponent
    and the player are penalized
    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    corners_list = [(0,0), (6,6), (0,6), (6,0)]
    own_moves = game.get_legal_moves(player)
    opo_moves = game.get_legal_moves(game.get_opponent(player))
    num_own_moves = len(own_moves)
    num_opo_moves = len(opo_moves)
    num_own_corners = 0
    num_opo_corners = 0
    for move in own_moves:
        if move in corners_list:
            num_own_corners += 1
    for move in opo_moves:
        if move in corners_list:
            num_opo_corners += 1
    return float((num_own_moves-num_own_corners)-(num_opo_moves-num_opo_corners))

def heuristic_4(game, player):
    """
    In this heuristic, if a player legal moves contains corners, the number of
    corners is substracted from the number of legal moves.This, to avoid
    selecting scenarios where the player heads to a corner. The current player
    is penalized and the opponent is rewarded

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    corners_list = [(0,0), (6,6), (0,6), (6,0)]
    own_moves = game.get_legal_moves(player)
    opo_moves = game.get_legal_moves(game.get_opponent(player))
    num_own_moves = len(own_moves)
    num_opo_moves = len(opo_moves)
    num_own_corners = 0
    num_opo_corners = 0
    for move in own_moves:
        if move in corners_list:
            num_own_corners += 1
    for move in opo_moves:
        if move in corners_list:
            num_opo_corners += 1
    return float((num_own_moves-num_own_corners)-(num_opo_moves+num_opo_corners))

def heuristic_5(game, player):
    """
    In this heuristic, the number of legal moves that are on a wall (max 4) are
    counted for both the player and the opponent. The score is calculated using
    the number of legal moves available - the number of moves in the walls as a
    way to penalize moves that lead to restricted movement. If the opponent
    has moves in the wall, it is rewarded, as we assume the opponent will avoid
    those moves.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    walls_list = [(0,0), (0,1),(0,2), (0,3),(0,4),(0,5),(0,6),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(1,6),(2,6),(3,6),(4,6),(5,6)]

    own_moves = game.get_legal_moves(player)
    opo_moves = game.get_legal_moves(game.get_opponent(player))
    num_own_moves = len(own_moves)
    num_opo_moves = len(opo_moves)
    num_own_walls = 0
    num_opo_walls = 0
    for move in own_moves:
        if move in walls_list:
            num_own_walls += 1
    for move in opo_moves:
        if move in walls_list:
            num_opo_walls += 1
    return float((num_own_moves-num_own_walls)-(num_opo_moves+num_opo_walls))

def heuristic_6(game, player):
    """
    In this heuristic,

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    walls_list = [(0,0), (0,1),(0,2), (0,3),(0,4),(0,5),(0,6),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6),(1,6),(2,6),(3,6),(4,6),(5,6)]

    own_moves = game.get_legal_moves(player)
    opo_moves = game.get_legal_moves(game.get_opponent(player))
    num_own_moves = len(own_moves)
    num_opo_moves = len(opo_moves)
    num_own_walls = 0
    num_opo_walls = 0
    for move in own_moves:
        if move in walls_list:
            num_own_walls += 1
    for move in opo_moves:
        if move in walls_list:
            num_opo_walls += 1
    return float((num_own_moves-num_own_walls)-(num_opo_moves-num_opo_walls))

def heuristic_7(game, player):
    """
    In this heuristic, the number of corners, walls(boxes in the edge of the
    board that are not corners), adjacent walls (boxes beside a wall), and boxes
    adjacent to the centre (and the centre included) are counted. The score
    returned is the number of moves available of the player adding the number of
    boxes adjacent to the centre and boxes adjacent to the walls and subtracting
    the number of walls and corners, this in an attempt to penalize paths that
    lead playing on walls and corners and rewarding paths moving in the areas
    where more moves are available.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    corners_list = [(0,0), (6,6), (0,6), (6,0)]
    walls_list = [(0,1),(0,2), (0,3),(0,4),(0,5),(1,0),(2,0),(3,0),(4,0),(5,0),(6,1),(6,2),(6,3),(6,4),(6,5),(1,6),(2,6),(3,6),(4,6),(5,6)]
    adj_wall_list = [(1,1),(1,2),(1,3),(1,4),(1,5),(5,1),(5,2),(5,3),(5,4),(5,5),(2,1),(3,1),(4,1),(2,5),(3,5),(4,5)]
    #The centre is included in this list
    adj_centre = [(3,3),(2,2),(2,3),(2,4),]
    own_moves = game.get_legal_moves(player)
    opo_moves = game.get_legal_moves(game.get_opponent(player))
    num_own_moves = len(own_moves)
    num_opo_moves = len(opo_moves)
    num_own_corners = 0
    num_opo_corners = 0
    num_own_walls = 0
    num_opo_walls = 0
    num_own_adj_walls = 0
    num_opo_adj_walls = 0
    num_own_adj_centre = 0
    num_opo_adj_centre = 0
    for move in own_moves:
        if move in corners_list:
            num_own_corners += 1
        if move in walls_list:
            num_own_walls += 1
        if move in adj_wall_list:
            num_own_adj_walls += 1
        if move in adj_centre:
            num_own_adj_centre += 1
    for move in opo_moves:
        if move in corners_list:
            num_opo_corners += 1
        if move in walls_list:
            num_opo_walls += 1
        if move in adj_wall_list:
            num_opo_adj_walls += 1
        if move in adj_centre:
            num_opo_adj_centre += 1
    return float((num_own_moves+num_own_adj_centre+num_own_adj_walls-num_own_walls-num_own_corners)-(num_opo_moves+num_opo_adj_centre+num_opo_adj_walls-num_opo_walls-num_opo_corners))

def get_max_path(game, player, depth):
    """
    Returns the max number of steps that a player can take with each legal move
    If the player can move more than 8 times, 8 is returned. The idea is to Find
    the paths were the players have few moves and not take them
    """
    max_path = 0
    legal_moves = game.get_legal_moves(player)
    if not legal_moves or depth == 0:
        return max_path
    for move in legal_moves:
        path = get_max_path(game.forecast_move(move),player,depth-1) + 1
        if path > max_path:
            max_path = path
        if max_path>8:
            break
    return max_path

def heuristic_8(game, player):
    """
    In this heuristic, the max path of a player is calculated. If a player has a
    longer path to travel than his opponent, he has a better chance to win.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")
    player_max_path = get_max_path(game, player, 8)
    oponent_max_path = get_max_path(game, game.get_opponent(player),8)
    if player_max_path == oponent_max_path:
        return 0
    return float(player_max_path-oponent_max_path)

def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: finish this function!
    # For my Heurisitc, I will define that float(-inf) will be a bad move
    # While float(inf) will be a good move
    return heuristic_7(game, player)
    #raise NotImplementedError


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        self.method = method
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves
        if not legal_moves:
            return (-1.-1)
        # MinMax and alphabeta return a list that contains a float and a tuple
        best_move_list = (None, (3,3))

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            if self.iterative:
                depth = 1
                # We iterate
                while True:
                    if self.method =='minimax':
                        best_move_list = self.minimax(game,depth)
                    else:
                        best_move_list = self.alphabeta(game,depth)
                    depth += 1
                    # If the score defined by my heuristic is positive
                    # that is the best move, I reach my goal and stop iterating
                    if best_move_list[0] == float('inf') or best_move_list[0] == float('-inf'):
                        break
            else:
                #We don-t want to iterate
                if self.method =='minimax':
                    best_move_list = self.minimax(game,self.search_depth)
                else:
                    best_move_list = self.alphabeta(game, self.search_depth)

        except Timeout:
            # no actions are necessary as we save the best move in each iteration
            pass
        # Return the best move from the last completed search iteration
        return best_move_list[1]
        #raise NotImplementedError

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # TODO: finish this function!
        legal_moves = game.get_legal_moves()
        # If I am on a leaf or I lost or won, I return the score
        if depth == 0 or not legal_moves:
            return self.score(game, self), (-1,-1)
        else:
            if maximizing_player:
                best_score = float('-inf')
                best_move = (-1,-1)
                for m in legal_moves:
                    score_tuple = self.minimax(game.forecast_move(m), depth-1,not maximizing_player)
                    score_result = score_tuple[0]
                    if best_score < score_result:
                        best_score = score_result
                        best_move = m
                return best_score, best_move
            # We want to minimize
            else:
                best_score = float('inf')
                best_move = (-1,-1)
                for m in legal_moves:
                    score_tuple = self.minimax(game.forecast_move(m), depth-1,not maximizing_player)
                    score_result = score_tuple[0]
                    if best_score > score_result:
                        best_score = score_result
                        best_move = m
                return best_score, best_move
        #raise NotImplementedError

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # TODO: finish this function!
        legal_moves = game.get_legal_moves()
        # If I am on a leaf or I lost or won, I return the score
        if depth == 0 or not legal_moves:
            return self.score(game, self), (-1,-1)
        else:
            if maximizing_player:
                best_move = (-1,-1)
                value = float('-inf')
                for m in legal_moves:
                    tmp_val = self.alphabeta(game.forecast_move(m), depth-1, alpha, beta, not maximizing_player)[0]
                    if value < tmp_val:
                        value = tmp_val
                        best_move = m

                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break
                return value, best_move
            # We want to minimize
            else:
                best_move = (-1,-1)
                value = float('inf')
                for m in legal_moves:
                    #value = min(value, self.alphabeta(game.forecast_move(m), depth-1,alpha, beta, not maximizing_player[0]))

                    tmp_val = self.alphabeta(game.forecast_move(m), depth-1, alpha, beta, not maximizing_player)[0]
                    if value > tmp_val:
                        value = tmp_val
                        best_move = m

                    beta = min(beta, value)
                    #best_move = m
                    if beta <= alpha:
                        break
                return beta, best_move
        #raise NotImplementedError
