# Git commands for terminal:

## 1.How to login in github:

## config --global user.email "you@example.com"

## 2.Creting a repo:

git init # It creats a new repo in cwd

git clone #Clones the github repo

## 3.Basics:

git status                  # check status of files
git add `<file>`              # stage file
git add .                   # stage all changes
git commit -m "message"     # commit staged changes
git log                     # view commit history
git log --oneline           # compact log

## 4.Dealing with branches:

git branch                  # list branches

git branch `<name>`           # create branch

git switch `<name>`           #  switch to branch

git merge `<branch>`          # merge into current branch

git branch -d `<name>`        # delete branch (safe)

git branch -D `<name>`        # force delete branch

## 5.Remote Repos:

git remote -v                       # list remotes
git remote add origin `<url>`         # add remote repo
git push -u origin main             # push first time
git push                            # push commits
git pull                            # fetch + merge changes
git fetch                           # only fetch (no merge)

## 6.ctrl+Z:

git restore `<file>`                  # discard changes in file

git restore --staged `<file>`         # unstage file

git reset --soft HEAD~1             # undo commit, keep changes staged

git reset --mixed HEAD~1            # undo commit, unstage changes

git reset --hard HEAD~1             # undo commit, discard changes

git checkout `<commit>` `<file>`        # restore file from commit

## 7.Tags or Version:

git tag v1.0                        # lightweight tag

git tag -a v1.0 -m "version 1.0"    # annotated tag

git show v1.0                       # show tag details

git push origin v1.0                # push single tag

git push origin --tags              # push all tags
