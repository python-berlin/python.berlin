# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

# Set canonical URL from the Read the Docs Domain
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

html_context = {}
# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    html_context["READTHEDOCS"] = True

project = "python.berlin"
copyright = "2025, Berlin Python User Groups"
author = "Berlin Python User Groups"
release = "2025.1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_sitemap",
]

templates_path = ["_templates"]
exclude_patterns = ["README.rst", "lib/*"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

# Change default HTML title
html_title = "Berlin Python User Groups"

html_static_path = ["_static"]
html_logo = "_static/images/logo/logo.png"
html_favicon = "_static/images/logo/favicon.ico"

# -- Linkcheck configuration -------------------------------------------------

linkcheck_ignore = [
    r"http://shop.oreilly.com/*",
]

# -- sitemap configuration ---------------------------------------------------

sitemap_url_scheme = "{link}"
sitemap_excludes = [
    "404.html",
    "search.html",
    "genindex.html",
]
sitemap_show_lastmod = True
