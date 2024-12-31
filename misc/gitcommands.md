# Terminology
Untracked files - files you don't intend to add to git (e.g., secrets files, .vscode settings files, api keys, your nudes) and/or files never yet added to git.

Changes not staged for commit - files at some point already added to git, changed on your branch/state, but not yet added to "this commit"

Changes to be committed - things you did `git add` to; you're stating your intention at your next `git commit` to commit these files to a point in time (a lil' node on that visual graph)


# Commands

`git status` - see what's currently staged, commited, whatever. Run this often.

`git add <location of file>` - add a specific thing "to be committed" - all that means is you're stating a file is something to be managed later.

` git commit -m <message>` - an informative message as to what was added, changed, whatever. Often but not necessarily right after this you'd do the below git push origin, but you can definitely have multiple commits on one branch before pushing.

`git push origin <name_of_branch>`- send that information to GitHub. You don't _need_ to do this, but it's good to make it visible online if you want my help.

`git fetch origin` - run this whenever you want to see if, or expect, I've added anything; it says "hey GitHub, you have anything new for me?"


# Your Workflow

* `main` is for completed days of work.
* `develop` is where you do an individual day's worth of work.

## Daily work
If you're _on_ `main`: (check with `git status` to see where you are, and your command line might show you too.)
`git checkout develop`

Do your git adds and commits and whatever _on develop_, then `git push origin develop` when done.

## When done with a day
If you're happy with the progress of that day, everything works, etc., and everything is already pushed to origin for develop:

`git checkout main`

`git merge --no-ff develop`

`git push origin main`

After which point you can and presumably should go back to `develop.`
