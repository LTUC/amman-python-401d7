from files_io import __version__

from files_io.in_out_files import read_file

def test_version():
    assert __version__ == '0.1.0'

def test_read_file():
    expected = "Hello Python devs\nLet's write some code\nThird line is here\n"
    actual = read_file('files_io/assets/spam.txt')
    assert actual == expected