#!/usr/bin/env python3

"""
Author: Jerônimo Bezerra
The script checks if there have been any modifications in the private repository and, if so, updates the local directory.
"""

import os
import sys
from git import Repo

# Configurations
USERNAME = "USER GIT"
REPO = "REPOSITORY NAME"
BRANCH = "main OR ANOTHER ONE"
LOCAL_DIR = "/PATCH/TO/FOLDER"
TOKEN = "YOUR TOKEN HERE"

def github_sync(directory):
    repo_path = os.path.join(directory, REPO)
    if os.path.exists(repo_path):
        # Local repository already exists, perform 'git pull'
        repo = Repo(repo_path)
        remote = repo.remote()
        remote.fetch()
        current_branch = repo.active_branch
        remote_branch = f"origin/{BRANCH}"

        if current_branch.name != BRANCH:
            # Switch to the desired branch
            repo.git.checkout(BRANCH)

        if repo.head.commit != repo.commit(remote_branch):
            # Perform 'git pull' if there are new commits
            repo.git.pull(remote, BRANCH)
            print("The local repository has been updated.")
            return 1
        else:
            print("The local repository is already up-to-date.")
            return 0
    else:
        # Local repository does not exist, perform 'git clone'
        repo_url = f"https://{TOKEN}@github.com/{USERNAME}/{REPO}.git"
        Repo.clone_from(repo_url, repo_path)
        print("The repository has been cloned.")
        return 1


if __name__ == "__main__":
    sys.exit(github_sync(LOCAL_DIR))
