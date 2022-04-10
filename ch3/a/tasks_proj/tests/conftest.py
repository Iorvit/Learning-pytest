import pytest

import tasks
from tasks import Task


# Reminder of Task cunstructor interface.
# Task(sammary=None, owner=None, done=False, id=None)
# summary is required.
# done and owner are otional.
# id is set by database


@pytest.fixture()
def tasks_db(tmpdir):
    """Connect to db before tests, disconnetc after."""
    # Setup : start db
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield  # this is where this testings happens.

    # Teardown : stop db
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_just_a_few():
    """All summarys and owners are unique."""
    return(
        Task('Write some code', 'Brain', True),
        Task("Code review Brain's code", 'Katie', False),
        Task('Fix what Brain did', 'Meshele', False),
    )


@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return(
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Creqte', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'),
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connect db with 3 tasks, all unique."""
    for task in tasks_just_a_few:
        tasks.add(task)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connect db with 9 tasks, 3 owners, all with 3 tasks."""
    for task_3 in tasks_mult_per_owner:
        tasks.add(task_3)
