gym_tetris
******

Tetris OpenAI gym environment.

Installing everything
---------------------

gym_tetris requires PyGame installed:

On OSX:

.. code:: shell

    brew install sdl sdl_ttf sdl_image sdl_mixer portmidi  # brew or use equivalent means
    conda install -c https://conda.binstar.org/quasiben pygame  # using Anaconda

On Ubuntu 14.04:

.. code:: shell

    apt-get install -y python-pygame

More configurations and installation details on: http://www.pygame.org/wiki/GettingStarted#Pygame%20Installation

And finally clone and install this package

.. code:: shell

    git clone https://github.com/lusob/gym-tetris.git 
    cd gym_tetris/
    pip install -e .

Example
=======

Run ``python example.py`` file to play tetris game with a random_agent (you need to have installed openai gym).

