from gym.envs.registration import registry, register, make, spec
from gym_tetris.tetris_env import TetrisEnv
# Pygame
# ----------------------------------------
for game in ['Tetris']:
    nondeterministic = False
    register(
        id='{}-v0'.format(game),
        entry_point='gym_tetris:TetrisEnv',
        kwargs={},
        timestep_limit=10000,
        nondeterministic=nondeterministic,
    )

