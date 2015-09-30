# -*- coding: utf-8 -*-
import sys, os
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig', 'sensio.sphinx.configurationblock']
source_suffix = '.rst'
master_doc = 'index'
project = 'JTL-Connector'
copyright = u'2010-2015, JTL-Software GmbH'
version = ''
release = ''
exclude_patterns = []
html_theme = 'connector_rtd_theme'
html_theme_path = ["_themes"]
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # overrides for wide tables in RTD theme
    ],
}

htmlhelp_basename = 'Connectordoc'
man_pages = [
    ('index', 'connector', u'JTL-Connector Documentation',
     [u'JTL-Software GmbH'], 1)
]
sys.path.append(os.path.abspath('_exts'))
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
primary_domain = 'php'
