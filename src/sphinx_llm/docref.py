from docutils.nodes import admonition
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective


class Docref(BaseAdmonition, SphinxDirective):
    node_class = admonition
    required_arguments = 1

    def run(self):
        doc_name = self.arguments[0]
        nodes = super().run()
        return nodes


def setup(app: Sphinx) -> dict:
    app.add_directive("docref", Docref)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
