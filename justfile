set ignore-comments
set export

DEPLOY           := justfile_directory() + "/deploy"
CONTENT          := justfile_directory() + "/docs"
PYTHON_REFERENCE := "/Users/peter/Repository/00-09 System/01 Org/reference/"
COMMIT_TAG       := `date "+%Y-%m-%dT%H:%M:%S"`


# List the available targets of this file
default:
    @just --list

################################################################################
# Development targets..
################################################################################
# Lint our markdown content files
lint:
    mdl --ignore-front-matter -s mdl_style.rb docs/posts/nano docs/posts/micro docs/posts/macro docs/posts/projects docs/posts/tech/emacs.md

# Run a local server to display pages (and update dynamically).
server:
    mkdocs serve

################################################################################
# Deployment targets..
################################################################################
# Preprocess org to markdown (our python environment file in particular)
preprocess:
    python org-md_preprocessor.py     --input "{{ PYTHON_REFERENCE}}/python-environment.org" --output "/tmp/python-environment.org"
    pandoc -f org -t gfm --wrap=none --output "/tmp/python-environment.md"                            "/tmp/python-environment.org"
    python org-md_postprocessor.py    --input "/tmp/python-environment.md"                   --output "{{CONTENT}}/posts/tech/python.md"

# Build our site in preparation for release
build:
    just preprocess
    mkdocs --verbose build

# Deploy the current version of the site
deploy:
    #!/usr/bin/env fish
    echo "Committing and pushing current build to github > {{COMMIT_TAG}}"
    echo "{{COMMIT_TAG}}"                              > git.log
    cd "{{DEPLOY}}" && git add --all .                >> git.log 2>&1
    cd "{{DEPLOY}}" && git commit -m "{{COMMIT_TAG}}" >> git.log 2>&1
    cd "{{DEPLOY}}" && git push -u origin main        >> git.log 2>&1
