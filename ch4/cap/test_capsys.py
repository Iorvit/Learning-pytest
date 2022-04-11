import sys


def greeting(name):
    print(f"Hi, {name}.")


def test_greeting(capsys):
    greeting("Geralt")
    out, err = capsys.readouterr()
    assert out == "Hi, Geralt.\n"
    assert err == ""

    greeting("Yennefer")
    greeting("Triss")
    out, err = capsys.readouterr()
    assert out == "Hi, Yennefer.\nHi, Triss.\n"
    assert err == ""


def yikes(problem):
    print("YIKES, {}".format(problem), file=sys.stderr)


def test_yikes(capsys):
    yikes("Out of coffee!")
    out, err = capsys.readouterr()
    assert out == ""
    assert "Out of coffee!" in err


def test_capsys_disabled(capsys):
    with capsys.disabled():
        print("\nalways print this.")
    print("normal print, usually captured.")
