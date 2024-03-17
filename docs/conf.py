# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import pathlib
import sys

this_path = pathlib.Path(__file__)
project_root = this_path.parent.parent.absolute()
project_src = project_root / "pyXsurf"

# according to below and https://sphinx-rtd-tutorial.readthedocs.io/en/latest/sphinx-config.html
sys.path.insert(0, str(project_src))

# -- Project information -----------------------------------------------------

project = "pyXsurf"
copyright = "2022, Vincenzo Cotroneo"
author = "Vincenzo Cotroneo"

# The full version, including alpha/beta/rc tags
with open(project_root / "VERSION") as version_file:
    release = version_file.read().strip()


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "myst_parser",
    "sphinx.ext.duration",
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx_automodapi.automodapi",
    "sphinx.ext.inheritance_diagram",
]


autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "**.ipynb_checkpoints"]

#  ----------- VC Sphinx Gallery settings according to https://sphinx-gallery.github.io/stable/getting_started.html#create-simple-gallery
# paths are relative to this file.
# sphinx_gallery_conf = {
# 'examples_dirs': 'examples',   # path to your example scripts
# 'gallery_dirs': 'gallery_auto_examples',  # path to where to save gallery generated output
# }

html_logo = "resources/Transparent Logo.png"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "bizstyle"

# VC
html_static_path = ["_static"]
html_css_files = [
    "custom.css",
]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_favicon = "resources/Favicon Original.ico"
