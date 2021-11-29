from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py")

@task
def robot(ctx):
    ctx.run("robot src/tests")


@task
def build(ctx):
    ctx.run("python3 src/initialize_database.py")
