from setuptools import setup, find_packages
import sys, os.path

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'gym_tetris'))

setup(name='gym_tetris',
      version=0.1,
      description='This package allows to play Tetris as a gym environment.',
      url='https://github.com/lusob/gym-tetris',
      author='Lusob',
      author_email='luis@sobrecueva.com',
      license='',
      packages=[package for package in find_packages()
                if package.startswith('gym')],
      zip_safe=False,
)
