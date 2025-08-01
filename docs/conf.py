import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'SIO Python for Earth Science Workshop'
author = 'Ellen Davenport'
release = '1.0'

html_title = "SIO Python for Earth Science"

extensions = [
    'nbsphinx',
    'myst_parser',  # optional if using .md instead of .ipynb
]
nbsphinx_execute = 'never'

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'furo'
html_static_path = ['_static']

