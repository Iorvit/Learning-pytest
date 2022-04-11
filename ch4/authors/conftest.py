"""Demonstrate tmpdir_factory."""

import json
import pytest


@pytest.fixture(scope="module")
def author_file_json(tmpdir_factory):
    """Write some authors to a data file."""
    python_author_data = {
        "Ned": {"City": "Boston"},
        "Brian": {"City": "Portland"},
        "Luciano": {"City": "Sao Paulo"},
    }

    file = tmpdir_factory.mktemp("data").join("author_file.json")
    print("file:{}".format(str(file)))

    with open(file, "w") as f:
        json.dump(python_author_data, f)

    return file
