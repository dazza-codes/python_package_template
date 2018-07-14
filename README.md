
## Python Template

A python library template.

## Development - Getting Started

- install `pyenv`, then
  - see https://github.com/pyenv/pyenv
  - `pyenv install 3.6.5`
  - `pyenv local 3.6.5`

- manage virtualenv and dependencies with pipenv
  - see https://docs.pipenv.org/basics/
  - `pip install --quiet pipenv`
  - `pipenv install --dev`
  - `pipenv check`
  - `pipenv shell` (use `exit` to end the session)

- run test suite
  - `python -m pytest tests`
