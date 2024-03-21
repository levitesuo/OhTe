from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)


@task
def max(ctx):
    ctx.run("python3 src/plaintxt_to_board_obj.py", pty=True)


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
def cov_r(ctx):
    ctx.run("coverage report -m")


@task
def build(ctx):
    ctx.run("python3 src/build.py")
