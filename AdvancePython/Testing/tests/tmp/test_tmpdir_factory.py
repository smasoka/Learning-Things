import os


def test_text_files(text_files):
    print(dir(text_files))
    assert "file1.txt" in str(text_files[0])
    assert "file2.txt" in str(text_files[1])
    assert 0
