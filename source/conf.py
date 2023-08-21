# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'REDi'
copyright = '2023, Arup'
author = 'Dr. Stevan Gavrilovic'
release = 'v1.0'
html_logo='./_static/Arup_Red_RGB.png'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

email_automode = True

#html_theme = 'sphinx_material'
#html_theme_options = {
#    'repo_url': 'https://github.com/arup-group/REDi',
#    'repo_name': 'REDi',
#    'html_minify': True,
#    'css_minify': True,
#    'nav_title': 'REDi',
#    'globaltoc_depth': 2,
#    'color_primary': 'blue',
#    'color_accent': 'light-blue',
#}

html_theme = 'pydata_sphinx_theme'

html_theme_options = {
 "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/arup-group/REDi",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fab fa-github-square",
            # Whether icon should be a FontAwesome class, or a local file
            "type": "fontawesome",  # Default is fontawesome
        }
   ],
   "show_toc_level": 3,
   "navbar_start": ["navbar-logo"],
   "navbar_center": ["navbar-nav", "project_name"],
   "navbar_end": ["navbar-icon-links"]
}
