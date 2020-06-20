import os


def test_create_file(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    # print(dir(p))
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1
    print(p)
    assert 0

# creates a py.path.local object
# offers os.path methods and more
