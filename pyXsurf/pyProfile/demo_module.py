from importlib_resources import files

"""
Define three functions respectively: returning a string; reading text from a file; reading text from a different file.
"""


def function():
    """return hardcoded string "pyProfile function"."""
    return "pyProfile function"


def data_function():
    """Return the contents of a text file
    "pyprofile_data.txt" located in the "pyProfile.data" package."""
    return files("pyProfile.data").joinpath("pyprofile_data.txt").read_text()


def common_data_function():
    """Return the contents of a text file "common_data.txt" located in the "data" package."""
    return files("data").joinpath("common_data.txt").read_text()
