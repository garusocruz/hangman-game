# Playing with chatGPT + Python + REACT
A friend and I decided to create a game using the chatGPT, our idea, was to explore the capabilities of AI, from game conception to code development.

We started talking to chatGPT to ideate something simple that didn't demand so much technical complexity, because we wanted to validate if the outputs would make sense. Then we came up with the hanging game, suggesting Caesar's Cipher to encrypt and decrypt the session and a base algorithm using random to select the game word as a parameter. 

For the Python backend, after some refinement of the prompt, we copy/pasted the results that chatGPT offered into the game engine, with some minor adjustments. Serving the endpoins with FAST-API using the route suggested by the AI. 

For the front end in REACT the use of the solutions made by chatGPT reached 90% requiring few code adjustments. Including the UI styles. Check it out the [code](https://github.com/garusocruz/vtg-game-app).

After a weekend, the colaboration with chatGPT resulted  in a simple and functional hanging game as you play clicking [here](https://gamming-hanging-react.web.app/). The biggest positive point is the speed in code creation and design decisions, highlighting the creation of the unit tests which saved about 80% of the time. The biggest negative point is the instability and unavailability of the system, which interrupted the development process when the history prompt had too many parameters or the cloud was congested.

I have read a lot that one of the big challenges of using AIs in general is mastering the creation of good prompts, but this is also true for any other tool, try cleaning a mirror with sandpaper to see what happens.
___
## hangman-game

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
