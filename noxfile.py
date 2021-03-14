import nox


@nox.session
def develop(session):
    session.install("-r", "requirements.txt")
    session.run("mkdocs", "serve")


@nox.session
def publish(session):
    session.install("-r", "requirements.txt")
    try:
        message = session.posargs[0]
    except IndexError:
        session.print("Did not publish - no change description. Replace MY-UPDATE in the following command: nos -s publish -- 'MY-UPDATE'")
    session.run("git", "add", "--all")
    session.run("git", "commit", "-m", repr(message))
    session.run("git", "push", "origin", "main")
    session.run("mkdocs", "gh-deploy")
