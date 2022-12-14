"""Проверим тип данных Task."""
from collections import namedtuple

Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


def test_defaults():
    """Без использования параметров, следует ссылаться на значение по умолчанию."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Проверка свойства .field (поля) namedtuple."""
    t = Task('Buy milk', 'Brian')
    assert t.summary == 'Buy milk'
    assert t.owner == 'Brian'
    assert (t.done, t.id) == (False, None)
