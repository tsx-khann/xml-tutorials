# Configuration file for the Sphinx documentation builder.

# -- Project Information -----------------------------------------------------

project = 'XML Tutorials'
author = 'THE GREAT KHAN'
copyright = '2021, xml'
version = '0.1.0'
release = '0.1'

# -- General Configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinx_rtd_theme"  # Use Read the Docs theme

# Enable dropdown menus in the sidebar
html_theme_options = {
    "collapse_navigation": False,  # Expands the menu instead of collapsing
    "navigation_depth": 3,         # Allows deeper levels in navigation
    "titles_only": False,          # Shows full titles instead of just headers
}

# Add custom CSS 
def setup(app):
    app.add_css_file('custom.css')

# -- Paths for static files -------------------------------------------------
html_static_path = ['_static']

# -- Options for EPUB output -------------------------------------------------

epub_show_urls = 'footnote'

# -- Remove "View page source" from the sidebar ----------------------------
html_sidebars = {
    '**': ['globaltoc.html', 'searchbox.html'],  # Remove 'source.html' to prevent page source viewing
}
