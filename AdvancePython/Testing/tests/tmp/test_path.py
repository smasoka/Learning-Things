import os

CONTENT = "content"


def test_create_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir() # create the temp dir
    # print(dir(d))
    p = d / "hello.txt"  # create the file in the temp dir
    # print(dir(p))
    p.write_text(CONTENT)
    assert p.read_text() == CONTENT
    assert len(list(tmp_path.iterdir())) == 1
    print(p)
    # assert 0

# For each test invocation
# tmp_path is a pathlib/pathlib2.Path object.
