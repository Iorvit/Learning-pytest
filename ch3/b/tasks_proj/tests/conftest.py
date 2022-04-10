import pytest

import tasks
from tasks import Task


# Reminder of Task cunstructor interface.
# Task(sammary=None, owner=None, done=False, id=None)
# summary is required.
# done and owner are otional.
# id is set by database


@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    """Connect to db before tests, disconnetc after."""
    temp_dir = tmpdir_factory.mktemp('temp')

    # Setup : start db
    tasks.start_tasks_db(str(temp_dir), 'tiny')

    yield  # this is where this testings happens.

    # Teardown : stop db
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """An empty tasks db."""
    tasks.delete_all()


@pytest.fixture(scope='session')
def tasks_just_a_few():
    """All summarys and owners are unique."""
    return(
        Task('Write some code', 'Brain', True),
        Task("Code review Brain's code", 'Katie', False),
        Task('Fix what Brain did', 'Meshele', False),
    )


@pytest.fixture(scope='session')
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
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)
