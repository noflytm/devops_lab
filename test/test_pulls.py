from handlers import pulls
import json
import nose


# https://nose.readthedocs.io/en/latest/testing_tools.html


def check_state(state):
    try:
        json.dumps(pulls.get_pulls(state))
    except ValueError:
        return False
    return True


def test_by_state():
    nose.tools.ok_(check_state('open'), True)
    nose.tools.ok_(check_state('closed'), True)


def test_by_label():
    nose.tools.ok_(check_state('needs work'), True)
    nose.tools.ok_(check_state('accepted'), True)


def test_responce_code():
    nose.tools.ok_(pulls.get_pulls('accepted')[0], 200)


def test_responce_code2():
    nose.tools.ok_(pulls.get_pulls('needs work')[0], 200)


if __name__ == '__main__':
    nose.run()
