from docutils.nodes import admonition
from docutils.parsers.rst.directives.admonitions import BaseAdmonition
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective


class Docref(BaseAdmonition, SphinxDirective):
    node_class = admonition
    required_arguments = 1

    def run(self):
        # Look up the document contents using the directive argument
        [doc_name] = self.arguments
        doc_contents = self.state.document.settings.env.app.builder.env.get_doctree(doc_name).astext()

        # Generate a summary of the document contents and replace the directive content with it
        summary = self.generate_summary(doc_contents)
        self.content.data = [summary]

        # Run the base admonition directive
        return super().run()
    
    def generate_summary(self, text: str) -> str:
        # TODO Generate summary from text
        # TODO Store the summary in a cache to avoid regenerating it
        return "WIP This will be an amazing summary!"



def setup(app: Sphinx) -> dict:
    app.add_directive("docref", Docref)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
