import nox


@nox.session(python=False)
def install(session):
    session.run("poetry", "install")
    session.run("poetry", "run", "pre-commit", "install")


@nox.session(python=False)
def tests(session):
    session.run("poetry", "run", "coverage", "run", "-m", "pytest")
    session.run("poetry", "run", "coverage", "html")
    session.run("poetry", "run", "coverage", "report")


@nox.session(python=False)
def lint(session):
    session.run("poetry", "run", "black", "--check", ".")
    session.run("poetry", "run", "flake8", ".")


@nox.session(python=False)
def typing(session):
    session.run("poetry", "run", "mypy", ".")


@nox.session(python=False)
def format(session):
    session.run("poetry", "run", "black", ".")


@nox.session(python=False)
def run(session):
    session.run("poetry", "run", "python", "greetings_app/entrypoints/app.py")
