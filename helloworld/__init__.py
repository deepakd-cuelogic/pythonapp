up vote
254
down vote
accepted
You can create tags for GitHub by either using:

the Git command line, or
GitHub's web interface.
Creating tags from the command line

To create a tag on your current branch, run this:

git tag <tagname>
This will create a local tag with the current state of the branch you are on. When pushing to your remote repo, tags are NOT included by default. You will need to explicitly say that you want to push your tags to your remote repo:

git push origin --tags
From the official Linux Kernel Git documentation for git push
