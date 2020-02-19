# My Python-Workspace
Vsc and Git works finaly together, me so happy.

https://youtu.be/9cMWR-EGFuY
Vid fel: https://help.github.com/en/github/authenticating-to-github/error-permission-denied-publickey

You should verify your connection by typing:
$ ssh -T git@github.com
> Hi username! You've successfully authenticated...

https://help.github.com/en/github/using-git/changing-a-remotes-url

Open Git Bash.

Change the current working directory to your local project.

List your existing remotes in order to get the name of the remote you want to change.

$ git remote -v
> origin  git@github.com:USERNAME/REPOSITORY.git (fetch)
> origin  git@github.com:USERNAME/REPOSITORY.git (push)
Change your remote's URL from SSH to HTTPS with the git remote set-url command.

$ git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
Verify that the remote URL has changed.

$ git remote -v
# Verify new remote URL
> origin  https://github.com/USERNAME/REPOSITORY.git (fetch)
> origin  https://github.com/USERNAME/REPOSITORY.git (push)
The next time you git fetch, git pull, or git push to the remote repository, you'll be asked for your GitHub username and password.
