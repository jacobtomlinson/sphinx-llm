# sphinx-llm

> [!WARNING]  
> This repo is experimental. Use at your own risk!

The `sphinx-llm` package includes extensions for leveraging LLMs as part of the Sphinx build process. 
This is useful for generating content that gets baked into the documentation. It it not intended to provide
an interactive chat service in your documentation.

## Installation

```console
pip install git+https://github.com/jacobtomlinson/sphinx-llm.git
```

## Usage

To use this extension you need to have [ollama](https://github.com/ollama/ollama) running.

If you have a GPU then generation will be much faster, but it is optional. See [the GitHub Actions](.github/workflows/build-docs.yml) for an example of using it in CI.

### Docref

The `sphinx_llm.docref` extension adds a directive for summarising and referencing other pages in your documentation.
Instead of just linking to a page the extension will generate a summary of the page being linked to and include that too.

![](docs/source/_static/images/pig-feeding-summary.png)

To use the extension add it to your `conf.py`.

```python
# conf.py
# ...

extensions = [
    "sphinx_llm.docref",
]
```

Then use the `docref` directive in your documents to reference other documents.

```rst
Testing page
============


.. docref:: apples
   
   Summary of apples page.
```

Then when you run `sphinx-build` (or `make html`) a summary will be generated and your source file will be updated.

```rst
Testing page
============


.. docref:: apples
   :hash: 31ec12a54205539af3cde39b254ec766
   :model: llama3.2:3b
   
   Feeding apples to a friendly pig involves selecting ripe, pesticide-free apples, washing them thoroughly, cutting into manageable pieces, introducing them calmly, monitoring the pig's reaction, and cleaning up afterwards.
```

A hash of the referenced document is included to avoid generating summaries unnecessarily. But if the referenced page changes the summary will be regenerated.

You can also modify the summary if you need to clean up the language generated, and as long as the hash still matches the file it will be used.

## Building the docs

Try it out yourself by building the example documentation.

```console
uv run --with sphinx-autobuild sphinx-autobuild docs/source docs/build/html
```
