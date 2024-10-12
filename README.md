# Greetings app

This is just simple flask app which goal is to present how to setup
CI/CD for Python application

## Prerequisites

Python at least 3.11 configured, poetry and nox.

After installing python
(for mac:

```
brew install python@3.11
```

for ubuntu

```
sudo apt-get install python@3.11
```

)

run

```
pip install poetry nox
```

## Install

```
nox -e install
```

## Run

```
nox -e run
```

Go to http://localhost:5000

## Test

```
nox -e tests
```

## Lint

```
nox -e lint
```

## Typing

```
nox -e typing
```

