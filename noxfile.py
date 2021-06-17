import nox

@nox.session(python=None)
def docs(session):
    session.install("doit", "importnb", "jupyter-book", "rich", "sphinx_sitemap")
    session.run("doit", "docs")