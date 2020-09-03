# -*- coding: utf-8 -*-
import sys, os

sys.path.append(os.path.abspath('_exts'))

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig']
source_suffix = '.rst'
master_doc = 'index'
project = 'JTL-Connector'
copyright = u'2010-2020, JTL-Software GmbH'
version = ''
release = ''
exclude_patterns = []
html_theme = 'connector_rtd_theme'
html_theme_path = ["_themes"]
html_show_sourcelink = False

htmlhelp_basename = 'Connectordoc'
man_pages = [
    ('index', 'connector', u'JTL-Connector Documentation',
     [u'JTL-Software GmbH'], 1)
]

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)

#primary_domain = 'php'
