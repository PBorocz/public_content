---
tags: 
  - make
  - just
---

# "Just" vs. Makefiles
After spending **another** 10 minutes trying to figure out more Makefile idiosyncrasies just to try and automate (and document) both oft and seldom issued commands, I recently found and decided to give the [Just](https://github.com/casey/just) command-line runner a try.

The [Just](https://github.com/casey/just) package took less than 10 minutes to understand what was necessary to change my complex Makefile to a far-simpler `justfile`.

**TL;DR;** -> Why has it taken me so long to find this! If you don't need to worry about _dependencies_, unreservedly recommended.

### My Previous Site's `justfile`

Here is the automation file that I used to build my previous site with [Hugo](https://gohugo.io "Hugo"):

```make

# Setup local variables
CONTENT    := justfile_directory() + "/content" # (1)
DEPLOY     := justfile_directory() + "/deploy"
COMMIT_TAG := `date "+%Y-%m-%dT%H:%M:%S"`


# This list of available targets # (2)
default: # (3)
    @just --list

# Build local content *and* deploy to public github repo.
deploy: build push  # (4) 

# Build local content to public directory.
build:
	@echo "Generating site..." # (5)
	@cd {{CONTENT}} && hugo --quiet --minify --gc --cleanDestinationDir -d {{DEPLOY}}  # (6)
	@cp {{CONTENT}}/CNAME {{DEPLOY}}

# Commit current version of local public directory and push to github.
push:
	@echo "Committing and pushing to github..."
	@cd {{DEPLOY}} && git add --all .                1>git.log  2>git.err  # (7)
	@cd {{DEPLOY}} && git commit -m "{{COMMIT_TAG}}" 1>>git.log 2>>git.err
	@cd {{DEPLOY}} && git push -u origin main        1>>git.log 2>>git.err

# Run a local server (including drafts).
server:
	@cd {{CONTENT}} && hugo server --buildDrafts --disableFastRender # (8)
```

1. :man_raising_hand: You can have local variables to represent common strings within the `justfile` (I treat them like shell variables). Similarly, there are a set of `just` specific methods, here, I'm getting the directory containing the `justfile` itself.

2. :man_raising_hand: A comment above a target will be the contents of the respective "help" command (see sample execution below).

3. :man_raising_hand: The `default` target will be executed when no target is specified on the invocation of `just`. In this case, we simply list the commands available in this `justfile`.

4. :man_raising_hand: To execute other targets, simply list them! In this case, a `deploy` action is actually composed of a `build` followed by a `push` target.

5. :man_raising_hand: The `@` symbol doesn't display the text of the command executed.

6. :man_raising_hand: Good example of running a command in another directory (there's no state carried from one command-line to the next).

7. :man_raising_hand: Good example of redirecting both stdout *and* stderr.

8. :man_raising_hand: Commands don't have to "end", here, the hugo server will continue to run until a CTRL-C.

---

``` bash
$ just
Available recipes:
    build   # Build local content to public directory.
    default # This list of available targets
    deploy  # Build local content *and* deploy to public github repo.
    push    # Commit current version of local public directory and push to github.
    server  # Run a local server (including drafts).
$ just build
  ...
```

**...no more `PHONY`'s!**

Now, obviously, since you're able to see the footer, you can tell I don't use Hugo anymore...thus, the need to do all the rigamorale above has gone away but `justfiles` continue to be a core component of every one of my projects.
