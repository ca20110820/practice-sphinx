"""Module containing the Game class.

This will contain a board instance inside as a composition.

It has a general implementation that can be integrated with different UI Views.
"""

from __future__ import annotations

from tictactoe.board import Board, BoardInvalidMove


class Game:
    """Class representing a Game instance.

    Attributes:
        player1 (str): Player 1 Name
        player2 (str): Player 2 Name
        player_moves (dict): Move labels of each player
        board (Board): NxN Board
    """
    def __init__(self, board_size=3, player1: str = "player1", player2: str = "player2", blank_label="?"):
        self._winner = None
        self._player = player1  # Initial player will always be player1
        self._game_iteration = 0

        self.player1 = player1
        self.player2 = player2
        self.player_moves = {player1: "X", player2: "O"}  # Player Name and their associated Move Labels

        self.board = Board(board_size, blank_label=blank_label)

    @property
    def winner(self):
        """Gets the winner of the game, if applicable.

        Returns:
            str | None: Winner if exists.
        """
        return self._winner

    @property
    def players(self):
        return [self.player1, self.player2]

    @property
    def current_player(self):
        return self._player

    @property
    def game_iteration(self):
        return self._game_iteration

    def _update_game_iteration(self):
        self._game_iteration += 1

    def _update_player(self):
        self._player = self.player1 if self._player == self.player2 else self.player2

    def print_game_state(self):
        self.board.print_grid()

    def move(self, row: int, col: int) -> str | None:
        """Make a move for a current player.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            str | None: The name of the winning player if there is one, 'finished' if the game is over without a winner,
            or None if the move is valid & goes to the next game state.

        Raises:
            BoardInvalidMove: If the move is invalid because a winner has already been determined.
        """
        # Returns: {self.player1, self.player2, 'finished', None}

        if isinstance(self.winner, str):
            raise BoardInvalidMove(f"There's already a winner for this game instance (Player: '{self.winner}').")

        self.board.update_grid(self.player_moves[self.current_player], row, col)

        winning_move = self.board.check_win()  # X, O, or None
        if isinstance(winning_move, str):
            self._winner = self.player1 if winning_move == "X" else self.player2
            self._update_game_iteration()
            return self._winner

        if self.board.is_board_filled:
            # Return 'finished' when no one won the game.
            self._update_game_iteration()
            return "finished"

        # TODO: Collect Data here before updating the state of the game.
        # ...

        self._update_player()
        self._update_game_iteration()
