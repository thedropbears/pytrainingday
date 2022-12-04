# 2023 programming training session

The Drop Bears' repository for training in using git, python, robotpy and such

## Install dependencies

	pip3 install -r requirements-sim.txt

## pre-commit

This project has [pre-commit.com](https://pre-commit.com) set up.

## Code style

This codebase adheres to the code style enforced by the black autoformatter:

    black .

This is enforced by CI. To install this:

    pip3 install black

See [PEP 8](https://www.python.org/dev/peps/pep-0008/) on naming conventions.

[Docstrings should follow Google style](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods).
See also [PEP 257](https://www.python.org/dev/peps/pep-0257/).

## Run

### Simulation (desktop)

    python robot.py sim

### Deploy to robot

    python robot.py deploy

This project is configured to automatically deploy to 4774's robot.


faoiaoidsfanulfgbaulifnhlauufihnsoc