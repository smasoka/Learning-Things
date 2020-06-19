import os
import pytest


@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        print(os.getcwd())
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        print(os.getcwd())

# 'cleandir' scope is function
# if its any hire, the tempfile created will cause assert 2 to fail
# because the temp directory will be used by all the functions in the test class

# fixtures on the class level.
# Functions inside class 'inherit' the fixture (its applied to all functions)
# Functions dont need to call the fixture fucntion individually. 
