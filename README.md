# Communication over Celery

## Installation
```
$ pip install - requirements.txt
```

### Execution
4 terminals are needed to run.

1. Start Redis locally
```
$ brew install redis
$ redis-server
```

2. Celery Server
```
$ python main.py --mode celery
```

3. Listener
```
$ python main.py --mode listener
```

4. Open Python Shell
```
$ python
```

```python
>>> from tasks import add
>>> task = add.delay(1, 3) # Insert any numbers
```

## Notice
- Please install latest version(>= `1.2.0`) of flower, the celery monitoring tool.

## Refs.
- [testdriven.io - <i>The Definitive Guide to Celery and FastAPI<i/>](https://testdriven.io/courses/fastapi-celery/app-factory/)
