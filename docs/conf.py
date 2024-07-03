# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../diorwebsite'))
sys.path.insert(0, os.path.abspath('../shop'))

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'diorwebsite.settings'

# Setup Django
django.setup()


project = 'Dior-Django-Website'
copyright = '2024, Ayanda247'
author = 'Ayanda247'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', 'sphinx.ext.napoleon']

templates_path = ['shop/templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
