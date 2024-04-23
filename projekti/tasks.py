from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def test(ctx):
    ctx.run("pytest src", pty=True)


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest", pty=True)


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)


@task(coverage)
def covr(ctx):
    ctx.run("coverage report -m")


@task
def build(ctx):
    ctx.run("python3 src/build.py")


@task
def runEng(ctx):
    ctx.run("python3 src/dev_tool_engine.py")
