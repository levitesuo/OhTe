from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


""" poetry run invoke test
    poetry run invoke coverage-report
"""
