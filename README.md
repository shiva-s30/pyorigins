# pyorigins

Template repository for python.

Pyorigins [pyorx] is a template repository for python projects to quickstart development with readily available dev tools and project structure.

Key features:

* pyproject.toml -> To maintain project metadata, entrypoint scripts, depedency list, packaging, code tools
* uv -> Used for project management that includes managing python and resolving dependencies with focus on high performance
* .gitignore -> standard .gitignore for python from Github
* .vscode -> standard launch config, settings and extensions needed for python development
  * Optional -> Provided for users preferring VSCode for development
* typer cli based app defined in [`src/main.py`](https://github.com/shiva-s30/pyorigins/blob/main/src/main.py)
  * Ex: `uv run pyorx`
  * Note: Recommended to run uv sync to get the virtual env started with dependencies/cli
* basic project template created with src, tests, config, report dirs (To be used as per user discretion)


