---
tags:
  - python
---

\-**- Mode: org -**- -**- fill-column: 132 -**-

# Python Environment Standards and Setup Notes

Python project setup falls into that nebulous/gray area in that: (a) you don't do it often enough for it to become habit and (b) you don't want to forget your own best practice for how to do it the next time you need to!

These are my notes for the "hows" and "whats" of my python environment for reference.

NOTE: This file represents <u>my</u> practice for *MY* projects; I make no guarantees that these are suitable for anyone else!

## Philosophy

There are a plethora of packages, libraries and tools to support the Python "project" eco-system. My philosophy around their use revolves around the following precepts:

- I use the single, best tool for the every component (even it that requires more tools!). There's been a recent focus on moving single-use tools to "uber" tools. For example, how many tools now allow you to manage virtualenvs as well?
- This usually implies using only the *core* capability of each tool (and thus, stay orthogonal and independent from other tools). For example, while Poetry **can** do virtualenvs, I limit it's use for package management and project builds.

## Meta Tool(s)

My kit relies on a set of individually installed tools into each respective virtual environment. Often, we don't want these tools installed in projects themselves (even on a "dev" basis) and thus we rely upon the wonderful [pipx](https://pypa.github.io/pipx/) environment to manage them (hence, why we consider [pipx](https://pypa.github.io/pipx/) a "*meta-tool*")

## Tools

My current toolkit is composed of the following packages:

| Tool                                                                | Use                                                                                                                                                                                                                                                                  |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [pyenv](Https://Github.Com/Pyenv/Pyenv)                             | Manage various versions of python installed on my system (ie. irrespective of project, just a set of all the python versions currently used across all my projects).                                                                                                 |
| [poetry](Https://Python-Poetry.Org/)                                | Manage project & package management.                                                                                                                                                                                                                                 |
| [poetry-bumpversion](https://github.com/monim67/poetry-bumpversion) | Poetry plugin to manage version-strings in `__init__.py` from `pyproject.toml` (installed into poetry environment with `poetry self add ...`                                                                                                                         |
| [pre-commit](https://pre-commit.com/)                               | Run pre-commit code-quality checks (installed via [pipx](https://pipx.pypa.io/stable/), usually run automagically or manually from `pyproject.toml` poe task).                                                                                                       |
| [direnv](https://direnv.net/)                                       | Manage `PYTHON_PATH` and virtual-env activation/deactivation (with a cool twist for this to happen automagically, see below under `Direnv Configuration`).                                                                                                           |
| [poethepoet](https://poethepoet.natn.io/index.html)                 | Capture and trigger commonly-used commands from right within a `pyproject.toml` file (installed and run via [pipx](https://pipx.pypa.io/stable/)).                                                                                                                   |
| [ruff](https://github.com/charliermarsh/ruff)                       | Manage essentially all source code textual quality, ie. lint AND formatting (installed via [pipx](https://pipx.pypa.io/stable/) and run usually from [pre-commit](https://pre-commit.com/) and a respective [plugin](https://github.com/astral-sh/ruff-pre-commit)). |

Emacs support for ruff from [ruff-lsp](https://github.com/astral-sh/ruff-lsp).

Good reference:

- [Python packages with pyproject.toml and nothing else \| Simon Willison’s TILs](https://til.simonwillison.net/python/pyproject)

## Python Version Confirmation

``` shell
# Confirm version of python to use
pyenv versions

# To list those /available/ to install:
# pyenv install --list

# If we want *do* want to update, bring it down and set it as the global version
# (this is how we ensure that the version of on "python -m venv .venv" below uses this version)
# pyenv install a.b.c
# pyenv global  a.b.c
#
# Often, we'll have to upgrade pip as well (even though we use Poetry for our projects)
# pip install --upgrade pip

```

## Project Setup

This is listed above venv creation as for a virgin project, creating the project layout with `poetry` itself first is slightly more straightforward.

``` shell
# Change to directory 1 level up from new project area..
cd ~/Repository/10-19 Development/10 Development

# Create project..
poetry new <projectname>

# (or `poetry init` for existing projects ;-)

# If we plan on doing any package publishing or if we reinstalled poetry:
# poetry config virtualenvs.create false

# and setup our testpypi environment:
# 1 - First, where will we *push* test packages to testpypi:
# poetry config repositories.testpypi https://test.pypi.org/legacy/

# 2 - where will test installs from testpypi:
# poetry config repositories.test https://test.pypi.org/simple/

cd <projectname>
```

## Virtual Environment Creation

Virtual environment precepts I am <u>manic</u> about are:

- **ALL** virtualenvs are at the **top-level** of the respective project (same level as `.github`).
- **ALL** virtualenvs are named `.venv`.

``` shell
# Create venv
python -m venv --without-pip .venv
```

## Direnv Configuration

Make venv startups essentially automatic (while also setting `PYTHON_PATH` appropriately!)

➡ Cut/paste to `.envrc` at project's top level directory:

``` shell
export VIRTUAL_ENV=`pwd`/.venv
PATH_add "$VIRTUAL_ENV/bin"
```

➡ Followed by:

    % direnv allow

References:

- Obviously [direnv](https://direnv.net/) itself.
- [Activate Python VirtualEnv Automatically with Direnv](https://erick.navarro.io/blog/activate-python-virtualenv-automatically-with-direnv)

## Packages

``` shell
###########################################################
# Add packages relevant to all environments (ie. dev *and* production)
###########################################################
# add those relevant to all environments (ie. dev *and* production), e.g. loguru?
poetry add ...

##########################################################
# Add development environment only packages
##########################################################
# pre-commit code quality checks
poetry add pre-commit --group dev
...etc...

###########################################################
# If we've reinstalled Poetry, add any Poetry plug-ins
###########################################################
# This keeps <package>/__init__.py/__version__ in sync with pyproject.toml on `poetry version` commands:
poetry self add poetry-bumpversion  # https://github.com/monim67/poetry-bumpversion
# NOTE: We use a poetry environment that's *common* across our projects/packages,
#       Thus, once we've installed something like bumpversion, it should be available
#       to our entire environment (confirm with `python self show plugins`)
```

## Git

``` shell
# Setup git repo (needed for pre-commit's git hooks)
git init

# ...Pull a sample .gitignore file from my most recent project (eg. 10.18 as of now)
```

An alternate idea for .gitignore (from a reddit comment) is to turn your gitignore into a "gitinclude" (the filename is the same, the usage somewhat different), something like the following:

``` code
# Ignore all root items - this is not recursive!
/*

# Use the exclamation mark to unignore a folder (and it's subitems) or file
!src
!docs

# I like keeping my files separate and below the folders
!README.md
!pyproject.toml

# Of course you can still (recursively) ignore anything unneeded
*.egg-info
__pycache__
```

## `pyproject.toml` Configuration

### ruff

Obviously, in pyproject.toml, place the following stanzas:

``` toml
[tool.ruff]
line-length = 120 # Matches black
target-version = "py311"

select = [
       "ALL", # include ALL rules, including *NEW* ones
]

ignore = [
       # modules (order here is from Ruff documentation)
       "ANN",  # flake8-annotations (ie. type annotations!)
       "S",    # flake8-bandit
       "BLE",  # flake8-blind-except
       "FBT",  # flake8-boolean-trap
       "A",    # flake8-builtins (NO! We use "id" as an attribute, sue me...)
       "EM",   # flake8-errmsg
       "ISC",  # flake8-implicit-str-concat
       "ICN",  # flake8-import-conventions
       "T20",  # flake8-print (NO! Removes all print statements!!)
       "PT",   # flake8-pytest-style
       "RET",  # flake8-return
       "SIM",  # flake8-simplify
       "TID",  # flake8-tidy-imports
       "ARG",  # flake8-unused-arguments
       "DTZ",  # flake8-datetimez
       "ERA",  # eradicate
       "PD",   # pandas-vet
       "PGH",  # pygrep-hooks
       "PIE",  # flake8-pie

       # specific rules
       "D100"    , # No abide 'Missing docstring in public module'   message, sue me.
       "D102"    , # No abide 'Missing docstring in public method'   "
       "D101"    , # No abide 'Missing docstring in public class'    "
       "D103"    , # No abide 'Missing docstring in public function' "
       "D104"    , # No abide 'Missing docstring in public package'  "
       "D105"    , # No abide 'Missing docstring in magic method'    "
       "D107"    , # No abide 'Missing docstring in __init__ method' "
       "D211"    , # Get rid of conflict with D203
       "D213"    , # Get rid of conflict with D212 (leaving D212)
       "E402"    , # Get rid of message about imports not being at the top (need for flask blueprints)
       "F401"    , # Allows for imports without use (e.g. __init__.py)
       # "I001"    ,  # Driving me crazy!!! (Imports out of order and/or unsorted!)
       # "PLW0603" ,  # Allows for the few places we use Globals (2 in DB and 1 in Channels and 1 in query)
]

[tool.ruff.per-file-ignores]
"config.py" = [
       "N802",  # We want all Config properties to be uppercase (even if from a method)
       "N805",  # We have classmethods defined that use 'cls' as arg, not 'self'!
       ]

[tool.ruff.mccabe]
max-complexity = 12  # Might be a bit too aggressive but start here and then only increase as absolutely necessary.
```

### PreCommit (optional)

From a reddit thread:

``` shell
pre-commit install
git add .pre-commit-config.yaml
pre-commit run --all-files  # optional (to test pre-commit)

############################################################
# Note: the previous 3 lines could be put into justfile as
# well, see raindroppy's justfile for an example.
############################################################
# To update the pre-commit configuration file to the most
# recent tag/revision available for each tool:
pre-commit autoupdate [--repo https://github.com/psf/black] [--repo another done]...
# (do not forget to pre-commit install and then git add afterwards!)

############################################################
# Copy over code formatting configuration and setup pre-commit
# code cleansing (if necessary)
############################################################
cp ~/repository/10-19 development/10 development/.pre-commit-config.yaml .
```

Good article on setting up pre-commit -\> [Improve your Django Code with pre-commit](https://builtwithdjango.com/blog/improve-your-code-with-pre-commit).

1.  Some good ideas for pre-commit (gleaned from: [Reddit](https://www.reddit.com/r/Python/comments/1cc9wtr/what_are_your_favourite_precommit_hooks_and_why/)):

    - ruff
    - yelp's "detect secrets"
    - forbid-tabs
    - end-of-file-fixer

### pip-audit (under research)

[GitHub - pypa/pip-audit: Audits Python environments and dependency trees for …](https://github.com/pypa/pip-audit)

## Background, Links and How-To

### Python Version Management aka [pyenv](Https://Github.Com/Pyenv/Pyenv)

- [Managing multiple python versions with pyenv – real python](https://realpython.com/intro-to-pyenv/) (great overview and tips!)
- [Customizing pyenv behavior with hooks](https://www.daan.fyi/writings/pyenv-hooks)
- [Just use pyenv, stop using other package managers for python \| by daryan hans…](https://d-hanshew.medium.com/just-use-pyenv-stop-using-other-package-managers-for-python-93229aabc04e)
- [pyenv](https://github.com/pyenv/pyenv) [(good intro to pyenv)](https://opensource.com/article/20/4/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)

### Package Management aka [poetry](Https://Python-Poetry.Org/)

- [Good poetry cheat sheet](https://www.yippeecode.com/topics/python-poetry-cheat-sheet/)
- [Dependency management with python poetry](https://realpython.com/dependency-management-python-poetry/) (good overview article (with most commands listed))
- [Trigger article](https://medium.com/@vanflymen/blazing-fast-ci-with-github-actions-poetry-black-and-pytest-9e74299dd4a5) (poetry, github actions, pytest)
- [Good overall from scratch with pyenv, pyenv-virtualenv and poetry](https://medium.com/georgian-impact-blog/python-tooling-makes-a-project-tick-181d567eea44#1791)
- [Jacob Kaplan Moss's 2020 setup](https://jacobian.org/2019/nov/11/python-environment-2020/) (pyenv, pipx and poetry)
- [Poetry and direnv](https://rgoswami.me/posts/poetry-direnv/) (small integration layer between the 2)
- [Full direnv configuration wiki page/documentation](https://github.com/direnv/direnv/wiki/python)

1.  Package creation & deployment

    - [episode \#137: start using a build system & continuous integration in python](https://realpython.com/podcasts/rpp/137/)
    - [Brenton Cleeland - An open source Python project CI pipeline](https://brntn.me/blog/open-source-python-ci/)
    - [Using python-poetry to publish to test.pypi.org - stack overflow](https://stackoverflow.com/questions/68882603/using-python-poetry-to-publish-to-test-pypi-org)
    - [Publishing a package to pypi with poetry — ian wootten](https://www.ianwootten.co.uk/2020/10/20/publishing-a-package-to-pypi-with-poetry/)
    - [Automating pypi releases using poetry and github actions — ian wootten](https://www.ianwootten.co.uk/2020/10/23/publishing-to-pypi-using-github-actions/)

2.  How to install from testpypi with poetry ([reference so](https://stackoverflow.com/questions/73447611/how-do-i-install-packages-from-test-pypi-org-using-poetry))

    1.  Make sure config entry for "test" is in `~poetry config --list~`.

    2.  cd to the top level directory and `~poetry new <testprojname>~`.

    3.  `~cd <testprojname>~`; `~python -m venv .env~`; `~activate~`.

    4.  Add the following stanza to the `pyproject.toml` file:

        ``` toml
        [tool.poetry.source]
        name = "test"
        url = "https://test.pypi.org/simple/"
        secondary = true
        ```

        \[note that the name & url match that within the `~poetry config --list~` environment!\]

    5.  Now, we can: `~poetry add <package> --source test~`.

3.  Reference

    - [documenting python projects with sphinx and read the docs – real python](https://realpython.com/courses/documenting-python-projects-sphinx-read-the-docs/) (*2023-01-06 Fri\>*)

### Package Distribution to/via **PyPi**

Specifically, how to publish our build to **TestPyPi** (args: –dry-run for example)

``` shell
set -x PYPI_TEST_USERNAME <token>
set -x PYPI_TEST_PASSWORD <api_token_from_testpypi>

poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish --repository testpypi --username $PYPI_TEST_USERNAME --password $PYPI_TEST_PASSWORD {{args}}

# NOTE: To pip install _from_ TestPyPi and get the right packages, we need to add regular pypi as a supplemental
#       as the overwhelming majority of other required packages will NOT be available on TestPyPi.
# Ref : https://stackoverflow.com/questions/57405014/how-to-fix-no-matching-distribution-found-for-package-name-when-installing-o
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple <ourPackage>
```

### Other People's Approaches

1.  [Cookiecutter-poetry](https://fpgmaas.github.io/cookiecutter-poetry/)

    This is a cookiecutter repository to generate the file structure for a python project that uses poetry for its dependency management.

2.  References and other examples

    - [An opinionated Python boilerplate - Duarte O.Carmo](https://duarteocarmo.com/blog/opinionated-python-boilerplate)
    - [My Goldilocks Python Setup. A solution that’s just right for… \| by David Amos…](https://betterprogramming.pub/my-goldilocks-python-setup-904e8e0784d7)
    - [How I start every new Python backend API project](https://blog.szymonmiks.pl/p/how-i-start-every-new-python-backend-api-project/)

3.  Setting up python projects (detailed!)

    - [Setting up python projects: part i](https://johschmidt42.medium.com/setting-up-python-projects-part-i-408603868c08) (git, python environment, ide etc.)
    - [Setting up python projects: part ii](https://johschmidt42.medium.com/setting-up-python-projects-part-ii-c4bd84b709d1) (formatting, linting, command management with makefiles, ci, etc.)
    - [Setting up python projects: part iii](https://johschmidt42.medium.com/setting-up-python-projects-part-iii-56aafde8ae0b) (testing)
    - [Setting up python projects: part iv](https://johschmidt42.medium.com/setting-up-python-projects-part-iv-82059eba4ca4) (documentation, ci/cd)

4.  If installing pycurl, also execute the following (assuming fish shell)

    ``` shell
    set -gx ldflags  -l/usr/local/opt/openssl/lib
    set -gx cppflags -i/usr/local/opt/openssl/include
    ```
