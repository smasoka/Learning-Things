import pytest


@pytest.fixture(scope="session")
def text_files(tmpdir_factory):
    filedir = tmpdir_factory.mktemp("data")
    file1 = filedir.join("file1.txt")
    file2 = filedir.join("file2.txt")
    return file1, file2
