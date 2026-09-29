# Configuration file for Sphinx documentation generator.
# Generated automatically by sphinx-mkdocs-migrate from plan: synthetic
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))
sys.path.insert(0, os.path.abspath('..'))

project = 'Python JSON Logger'
copyright = 'Python JSON Logger Contributors'
author = 'Documentation Authors'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_immaterial',
]

source_suffix = {
    '.md': 'markdown',
}

html_theme = 'sphinx_immaterial'
html_title = 'Python JSON Logger'
html_baseurl = 'https://nhairs.github.io/python-json-logger'
autosummary_generate = False
add_module_names = False
autoclass_content = 'both'
exclude_patterns = ['.DS_Store', 'Thumbs.db', '_build']

html_theme_options = {   'edit_uri': 'tree/master/docs',
    'features': [   'navigation.instant',
                    'navigation.sections',
                    'navigation.indexes',
                    'navigation.expand',
                    'navigation.top',
                    'content.code.annotate',
                    'content.code.copy',
                    'toc.follow'],
    'globaltoc_collapse': False,
    'icon': {'logo': 'material/code-braces'},
    'palette': [   {   'primary': 'amber',
                       'scheme': 'default',
                       'toggle': {   'icon': 'material/weather-night',
                                     'name': 'Switch to dark mode'}},
                   {   'primary': 'amber',
                       'scheme': 'slate',
                       'toggle': {   'icon': 'material/weather-sunny',
                                     'name': 'Switch to light mode'}}],
    'repo_name': 'nhairs/python-json-logger',
    'repo_url': 'https://github.com/nhairs/python-json-logger',
    'site_url': 'https://nhairs.github.io/python-json-logger',
    'social': [   {   'icon': 'fontawesome/brands/github',
                      'link': 'https://github.com/nhairs/python-json-logger'}],
    'version_dropdown': True,
    'version_json': 'versions.json'}

object_description_options = [
    ('py:.*', dict(include_fields_in_toc=False)),
    ('py:parameter', dict(include_in_toc=False)),
]

myst_enable_extensions = [
    'colon_fence',
    'deflist',
]

myst_heading_anchors = 3


import re
_re_md_link = re.compile(r'(?<![!])\[(?P<text>[^\]\n]+?)\]\((?P<url>[^\)\s]+)\)')
_re_cross_ref = re.compile(r'(?<![!])\[(?P<text>[^\]\n]+?)\]\[(?P<target>[a-zA-Z_0-9\.]+)\]')
_re_empty_cross_ref = re.compile(r'(?<![!])\[(?P<target>[a-zA-Z_0-9\.]+)\]\[\]')
_re_md_code = re.compile(r'(?<![:`])`(?P<code>[^`\n]+?)`(?!_|\`)')

def process_docstrings(app, what, name, obj, options, lines):
    if what == 'module' and getattr(options, 'members', None):
        lines.clear()
        return
    for i in range(len(lines)):
        if '[' in lines[i] and '][' in lines[i]:
            lines[i] = _re_empty_cross_ref.sub(r':py:obj:`\g<target>`', lines[i])
            lines[i] = _re_cross_ref.sub(r':py:obj:`\g<text> <\g<target>>`', lines[i])
        if '[' in lines[i] and '](' in lines[i]:
            def repl(m):
                clean_text = m.group('text').replace('`', '').strip()
                return f'`{clean_text} <{m.group("url")}>`_'
            lines[i] = _re_md_link.sub(repl, lines[i])
        if '`' in lines[i]:
            lines[i] = _re_md_code.sub(r'``\g<code>``', lines[i])

def setup(app):
    app.connect('autodoc-process-docstring', process_docstrings)
