# hangman-game

## Environment

### create a virtual environment

```
python -m venv .venv
```

## load a virtual environment

```
source .venv/bin/activate
```

---

## Poetry manager dependency

### Install a poetry package manager

```
pip install poetry
```

### To add a new python package with poetry in dev group

```
poetry add --group dev  pre-commit
```

---

### To add a new python packagead default group

```
poetry add fast-api
```

### To install dependencies in your project

```
poetry install
```

### To start a fast api server application

```
poetry run server
```

### To start a fast api server application in another port

```
poetry run server --port=8001
```

---

## Pre-commit

To use pre commit you need to run the code bellow:

```
pre-commit install
```
