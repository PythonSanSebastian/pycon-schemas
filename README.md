# pycon-schemas

## How to collaborate

This project uses [pipenv](https://pipenv.readthedocs.io) to manage its dependencies
and Python environment. You can install it by:

```bash
pip install --user pipenv
```

We recommend using a Python virtual environment for each separate project you do.
For that, we suggest using [pyenv](https://github.com/pyenv/pyenv-installer).

### Installation

For development you should also install the development dependencies,
so run instead:

```bash
cd <clone_dest>
make install-dev
```

This will install all dependencies and this project in development mode.

### Testing

We use [tox](https://tox.readthedocs.io/en/latest/) to run the code checkers.

You can run the tests by running `tox` in the top-level of the project.
