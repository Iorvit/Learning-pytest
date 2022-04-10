import tasks
from tasks import Task


def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db.
    # WHEN a new task is added.
    # THEN returning task_if is of typy int.
    new_task = Task('do somethin')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() affect on tasks.count()."""
    # Given db with 3 tasks.
    # When another task is added.
    tasks.add(Task('throw a paty'))

    # THEN the count increases by 1.
    assert tasks.count() == 4
