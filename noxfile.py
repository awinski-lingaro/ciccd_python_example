import nox


@nox.session(python=False)
def tests(session):
    session.run("poetry", "shell")
    session.run("poetry", "install")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "html")
    session.run("coverage", "report")


@nox.session(python=False)
def lint(session):
    session.run("poetry", "shell")
    session.run("poetry", "install")
    session.run("black", "--check", ".")
    session.run("flake8", ".")


@nox.session(python=False)
def typing(session):
    session.run("poetry", "shell")
    session.run("poetry", "install")
    session.run("mypy", ".")


@nox.session(python=False)
def format(session):
    session.run("poetry", "shell")
    session.run("poetry", "install")
    session.run("black", ".")


@nox.session(python=False)
def run(session):
    session.run("poetry", "shell")
    session.run("poetry", "install")
    session.run("python", "greetings_app/entrypoints/app.py")
