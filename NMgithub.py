from git import *
import git
import subprocess
import os
import time
def fu():
    # repo = Repo.clone_from("https://github.com/nivek0119/netman_Lab5.git", "/home/kevin/Netman/Lab_5_Midterm/")
    # remote = repo.create_remote(remote_name, url=another_url)
    # remote.push(refspec='{}:{}'.format(local_branch, remote_branch))

    # hello
    # hello ack
    # repo = Repo(self.rorepo.working_tree_dir)
    # assert not repo.bare
    # from git import Repo
    # Repo.clone_from("https://github.com/nivek0119/netman_Lab5.git", "/home/kevin/Netman/Lab_5_Midterm")

    # def print_repository_info(repo):
    #     print('Repository description: {}'.format(repo.description))
    #     print('Repository active branch is {}'.format(repo.active_branch))

    #     for remote in repo.remotes:
    #         print('Remote named "{}" with URL "{}"'.format(remote, remote.url))

    #     print('Last commit for repository is {}.'.format(str(repo.head.commit.hexsha)))



    repo_path = "/home/kevin/Netman/Lab_5_Midterm"
    repo = Repo.init(repo_path)
    print(repo)

    # repo_dir = os.path.join(rw_dir, "my-new-repo")
    # file_name = os.path.join(repo_dir, "new-file")
    a=repo.index.add(["/home/kevin/Netman/Lab_5_Midterm/."])
    b=repo.index.commit("initial commit from git")
    print(a)
    print(b)


    # Add a remote named "origin"
    remote_url = 'https://github.com/nivek0119/netman_Lab5.git'
    print(remote_url)
    # z=repo.create_remote('origin', url=remote_url)
    # print(z)


    r1=remote = repo.remote('origin')

    # Push changes to the remote
    r2=remote.push(refspec="master")
    print(r1)
    print(r2)

    diff_output = repo.git.diff()
    print(diff_output)


    # r = git.Repo.init(repo_dir)
    # # This function just creates an empty file ...
    # open(file_name, "wb").close()
    # r.index.add([file_name])
    # r.index.commit("initial commit")

def gitInit():
    os.system("git init >/dev/null 2>&1")
    # https://github.com/nivek0119/t5.git

def gitAddAll():
    os.system("git add *")

def gitCommit():
    os.system("git commit -m 'message'")

def gitRemoteAddOrigin():
    os.system("git remote add origin https://github.com/nivek0119/t8.git >/dev/null 2>&1")

def gitpushOriginMaster():
    os.system("git push -u origin master")

def gitStatus():
    os.system("git status")

def gitDiff():
    print(os.popen("git diff @{upstream}").read())

# # gitStatus()
# print("Initializing Git")
# gitInit()
# print("")
# print("Adding All files in repo")
# gitAddAll()
# print("")
# print("Comminting All changes locally in repo")
# gitCommit()
# # gitRemoteAddOrigin()
# print("")
# print("Sending all commit changes to remote repo")
# gitpushOriginMaster()


# # gitStatus()
# print("")
# print("Showing Differences")
# gitDiff()

# time.sleep(10)
# print("")
# print("Adding All files in repo")
# gitAddAll()
# print("")
# print("Comminting All changes locally in repo")
# gitCommit()
# print("")
# print("Sending all commit changes to remote repo")
# gitpushOriginMaster()