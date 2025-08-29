from celery import Celery

app = Celery(
    main="tasks",
    broker="redis://localhost:6379/0",
    backend="db+sqlite:///celery.sqlite"
)


@app.task
def hello(name):
    message = f"Hello, {name}"
    return message
