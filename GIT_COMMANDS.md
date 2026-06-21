# 🚀 Git Commands Reference

A quick reference guide for common Git commands. Save this in your repository for easy access!

---

## 📋 Table of Contents

1. [Repository Setup](#-repository-setup)
2. [Basic Workflow](#-basic-workflow)
3. [Branching](#-branching)
4. [Remote Repositories](#-remote-repositories)
5. [Viewing History & Status](#-viewing-history--status)
6. [Undoing Changes](#-undoing-changes)
7. [SSH & Authentication](#-ssh--authentication)
8. [Troubleshooting](#-troubleshooting)

---

## 📁 Repository Setup

| Command | What it does |
| :--- | :--- |
| `git init` | Initializes a **new** Git repository in the current folder. |
| `git clone <url>` | Downloads an **existing** repository from GitHub (or other remote). |
| `git clone git@github.com:username/repo.git` | Clones using **SSH** (no password prompts after setup). |
| `git clone https://github.com/username/repo.git` | Clones using **HTTPS** (requires token/password). |

---

## 📝 Basic Workflow

### The 3-Step Process

```bash
git add <file>      # Stage specific file(s) for commit
git add .           # Stage ALL changes in current folder
git commit -m "message"  # Save changes locally with a message
git push origin <branch> # Upload to GitHub
Command	What it does
git status	Shows what's changed and what's staged.
git add <filename>	Stages a specific file for commit.
git add .	Stages all changed files in the current folder.
git add -A	Stages all changes everywhere in the repo.
git commit -m "message"	Saves staged changes with a descriptive message.
git push origin main	Uploads your commits to GitHub (main branch).
git pull	Downloads latest changes from GitHub.
🌿 Branching
Command	What it does
git branch	Shows all branches in your repo (* = current branch).
git branch <name>	Creates a new branch.
git checkout <branch>	Switches to another branch.
git checkout -b <branch>	Creates and switches to a new branch.
git merge <branch>	Merges another branch into the current one.
git branch -d <branch>	Deletes a branch (local).
🌐 Remote Repositories
Command	What it does
git remote -v	Shows all remote connections (fetch/push URLs).
git remote add origin <url>	Connects local repo to a remote (usually GitHub).
git remote set-url origin <new-url>	Changes the remote URL (e.g., from HTTPS to SSH).
git push -u origin main	Pushes and sets upstream (future pushes = just git push).
📊 Viewing History & Status
Command	What it does
git status	Shows current state of your working directory.
git log	Shows commit history (press q to exit).
git log --oneline	Shows compact 1-line commit history.
git log --graph	Shows history with a graph of branches.
git diff	Shows differences between working directory and staging.
git diff --staged	Shows differences between staging and last commit.
git show <commit-hash>	Shows details of a specific commit.
git blame <file>	Shows who changed which lines in a file.
↩️ Undoing Changes
Command	What it does
git restore <file>	Discards local changes to a file (reverts to last commit).
git restore --staged <file>	Unstages a file (keeps changes, but removes from staging).
git reset HEAD~1	Undoes the last commit (keeps changes locally).
git reset --hard HEAD~1	Undoes last commit AND discards changes (⚠️ permanent!).
git revert <commit-hash>	Creates a new commit that undoes a previous commit (safe).
git rm <file>	Removes a file from tracking and disk.
git rm --cached <file>	Removes a file from tracking but keeps it on disk.
🔑 SSH & Authentication
Command	What it does
ssh-keygen -t rsa -b 4096 -C "email@example.com"	Generates SSH key pair for GitHub authentication.
cat ~/.ssh/id_rsa.pub	Displays your public SSH key (copy to GitHub).
ssh -T git@github.com	Tests SSH connection to GitHub.
git config --global user.name "Your Name"	Sets global Git username.
git config --global user.email "you@example.com"	Sets global Git email.
git config --list	Shows all Git configuration.
🛠️ Troubleshooting
Problem	Solution
fatal: not a git repository	You're not in a Git repo. Run git init or cd to repo.
Authentication failed	Use SSH or Personal Access Token (not password).
remote: Repository not found	Check repository name / URL, or create it on GitHub first.
Please tell me who you are	Run git config --global user.name and user.email.
Your branch is ahead of 'origin/main'	Run git push to upload your commits.
Your branch is behind 'origin/main'	Run git pull to download latest changes.
⚡ Quick Cheat Sheet
Most common commands (copy-paste ready):
bash
# After making changes:
git add .
git commit -m "Description of changes"
git push origin main

# Before making changes (get latest):
git pull

# Check what's happening:
git status
git log --oneline

# Switch branches:
git checkout other-branch

# Connect to GitHub (SSH):
git remote add origin git@github.com:username/repo.git
🎯 Commands for this course (your specific setup)
For DACA-portfolio:
bash
cd ~/Desktop/Kursus/Repositary/DACA-portfolio
git add .
git commit -m "Add new content"
git push origin main
For DACA-group:
bash
cd ~/Desktop/Kursus/Repositary/DACA-group
git add .
git commit -m "Add new content"
git push origin main
📚 Pro Tips
Always git status before committing – see what you're about to save.

Write meaningful commit messages – future you will thank you.

Pull before you push – avoid conflicts.

Never commit sensitive data (passwords, tokens). Use .gitignore.

Create a .gitignore file to exclude temporary files:

bash
touch .gitignore
echo "__pycache__/" >> .gitignore
echo "*.log" >> .gitignore
