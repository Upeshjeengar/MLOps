#  Practicising Git commands

### Basic setup 
* Defining the user name  
`git config --global user.name upesh`   
* Defining the email   
`git config --global user.email vikashdas770@gmail.com`   
* check your user name   
`git config --global user.name`   
* check your email   
`git config --global user.email`

### Pushing to local repository

* Add file: `git add .` or `git add <filename>`
* Check status of all files in current directory : `git status`
* Check commit history: `git log`
* Track commit history: `git log --oneline`(returns hashed string to easily track or move back), to track back from this SHA id: `git show <sha_id>`
* Tracks file by file changes: `git log --stat`
* Track line by line change in a file: `git log -p`
* To see Changes made after last commit: `git diff`
* Roll back to some previous version `git checkout <sha_id>`
* If you roll back to a previous version you need to make it master branch to further proceed.


### Branching and Merging
* Create a new branch named _'helper'_: `git branch helper` 
* See status: git branch(shows all active branches)

* We are at head of main and helper branch now we will shift to helper branch using `git checkout helper` add some commits to both branches

* To see all commits in master and helper branch: `git log --oneline --all` or `git log --oneline --all --graph` for better understanding
* Use this command to delete other branches: `git branch -d helper`, if any unsaved changes remaining in helper it will raise error.
* To force delete unmerged changes of helper use `git branch -D helper`(to force delete you have to leave helper branch)

### Merge conflict
* Create a branch named `final` and make some changes to helper.py and checkout to master and make some changes there and now if you `git merge final` you'll get error
* You can choose any action: Accept Current Change | Accept Incoming Change | Accept Both Changes | Compare Changes

### Working with Remote repo and versioning