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

### Working with Remote repo 
1. git remote add origin <url> (declaring remote repo) 
2. git push origin master/main (sends local repo to origin) 
3. git pull origin master (pull code from remote repo) 
4. git clone <url> (download/copy remote repo)

### Versioning
1. git tag -a v1.0.0 <sha(optional)>   
Vim editor:   
Fn+insert -- write a message   
:wq – save and quit 
2. git log (check if tagging was done successfully) 
3. git tag -d v1.0.0 (delete the mentioned tag)


# In organization git learnings:
# Demo Project file



### Git History and Creating Custom Git Commands with Aliases
Will set hist as new command
`git config --global alias.hist "log --online --graph --decorate --all"`. 

* Renaming file: ```git mv old_file_name new_file_name```

* Removing file: `git rm file_name`

### Git Branch Operations

#### Checkout a Branch
```git checkout branch_name```
- **Purpose**: Switches your working directory to the specified branch
- **Parameters**:
  - `branch_name`: The name of the branch you want to switch to
- **Returns**: Confirmation message when successfully switched to the branch

#### Merge Changes
```git merge branch_name```
- **Purpose**: Integrates changes from the specified branch into your current branch
- **Parameters**:
  - `branch_name`: The name of the branch whose changes you want to merge (e.g., main)
- **Returns**: Confirmation of successful merge or conflict notifications if applicable

#### Create a Tag
```git tag v0.1```
- **Purpose**: Creates a lightweight tag at the current commit
- **Parameters**:
  - `v0.1`: The name of the tag (typically version numbers)
- **Returns**: No output if successful

* Switch to the specified branch
```git checkout branch_name```

Merge changes from another branch (e.g., main)
* ```git merge (from main)```

* Create a new tag named v0.1
```git tag v0.1```

* Save changes temporarily without committing
```git stash```

* List all stashed changes
```git stash list```

* Undo commits, keep changes staged
```git reset commit_id --soft```

* Undo commits, keep changes unstaged
```git reset commit_id --default```

* Undo commits, keep changes in working directory
```git reset commit_id --mixed```

* Undo commits and discard all changes
```git reset commit_id --hard```


`````` 
`````` 
