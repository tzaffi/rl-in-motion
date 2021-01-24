import numpy as np
from typing import Tuple


class Maze:
    def __init__(self, wall_coords):
        self.m, self.n = 6, 6
        self._maze = np.zeros((self.m, self.n))
        self._maze[wall_coords] = 1

        self.robot_position = (0, 0)

    def get_maze(self):
        maze = self._maze.copy()
        maze[self.robot_position] = 2
        return maze

    def print_maze(self):
        pass

    def update_maze(self, action):
        pass

    def is_game_over(self):
        pass

    def get_state(self):
        pass

    def give_reward(self, state):
        """
        Not sure I agree you need the state as a param, since already embedded in the robot_position
        """
        pass


def test_Maze():
    assert False, "gotta actually fill the class out and write some real tests"


class ZMaze:
    def __init__(self, wall_coords):
        self.m, self.n = 6, 6
        self.maze = np.array([[" "] * self.n] * self.m)
        for i, j in wall_coords:
            self.maze[i][j] = "X"
        self.state = np.array([0, 0])

    def get_state(self) -> np.array:
        return self.state.copy()

    def __str__(self):
        maze = self.maze.copy()
        i, j = self.state
        maze[i][j] = "R"
        div = "+" + "-" * (2 * self.n - 1) + "+\n"
        rows = [f"|{row}|\n" for row in ("|".join(maze[i]) for i in range(self.m))]
        return f"{div}{div.join(rows)}{div}"

    def game_over(self) -> bool:
        return self.maze[self.m][self.n] == "R"

    @classmethod
    def _move2vec(cls, move: str) -> np.array:
        assert move in ["r", "l", "u", "d"], f"unrecognized move {move}"
        if move == "r":
            return np.array([0, 1])
        if move == "l":
            return np.array([0, -1])
        if move == "u":
            return np.array([-1, 0])
        return np.array([1, 0])

    def _element_at(self, state: np.array) -> str:
        return self.maze[tuple(state)]

    def move_allowed(self, move: str) -> Tuple[bool, np.array]:
        move = self._move2vec(move)
        next_state = self.state + move
        if any(next_state < 0) or next_state[0] >= self.m or next_state[1] >= self.n:
            return False, next_state
        if self._element_at(next_state) == "X":
            return False, next_state
        return True, next_state

    def update(self, move: str) -> np.array:
        allowed, next_state = self.move_allowed(move)
        assert allowed, f"cannot move to {tuple(next_state)}"

        self.state = next_state.copy()
        return next_state

    def get_rewards(self) -> float:
        pass


def test_ZMaze():
    print(ZMaze([]))

    m = ZMaze(
        [
            (0, 5),
            (1, 5),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (3, 2),
            (3, 5),
            (5, 0),
            (5, 1),
            (5, 2),
            (5, 3),
            (5, 4),
            (5, 5),
        ]
    )
    print(m)

    allowed, next_state = m.move_allowed("r")
    assert allowed
    assert np.array_equal(next_state, np.array([0, 1]))

    allowed, next_state = m.move_allowed("l")
    assert not allowed
    assert np.array_equal(next_state, np.array([0, -1]))

    allowed, next_state = m.move_allowed("d")
    assert allowed
    assert np.array_equal(next_state, np.array([1, 0]))

    allowed, next_state = m.move_allowed("u")
    assert not allowed
    assert np.array_equal(next_state, np.array([-1, 0]))

    m = ZMaze(
        [
            (0, 1),
            (0, 5),
            (1, 5),
            (2, 2),
            (2, 3),
            (2, 4),
            (2, 5),
            (3, 2),
            (3, 5),
            (5, 0),
            (5, 1),
            (5, 2),
            (5, 3),
            (5, 4),
            (5, 5),
        ]
    )
    print(m)

    allowed, next_state = m.move_allowed("r")
    assert not allowed
    assert np.array_equal(next_state, np.array([0, 1]))


test_Maze()
test_ZMaze()
