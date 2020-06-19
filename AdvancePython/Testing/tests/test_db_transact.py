import pytest


# in a seperate file - DB.py
class DB:
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        self.intransaction.append(name)

    def rollback(self):
        self.intransaction.pop()


# in conftest.py
@pytest.fixture(scope="module")
def db():
    return DB()


# in test_db_transct.py
class TestClass:
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        db.begin(request.function.__name__)
        print("yielding now ......")
        yield
        db.rollback()

    def test_method1(self, db):
        print("test_method1")
        assert db.intransaction == ["test_method1"]

    def test_method2(self, db):
        print("test_method2")
        assert db.intransaction == ["test_method2"]

# The class-level transact fixture is marked with autouse=true
# which implies that all test methods in the class will use this fixture function
# without a need to state it in the test function signature
# or with a class-level usefixtures decorator.
