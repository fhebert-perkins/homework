# homework
This is where homework assignments will be posted and submitted.

Please submit your code for Questions 2, 4, 5 and 6.  Question 7 is optional.  Due 3/21/2016 12:40pm
# How to use git
We have created an organization called "15-16bayCS2", and a repository within that organization called "homework".  The homework respository has several "branches", one called "master" and one for each student.  If you haven't already, ask a git-maven to create a branch of master called [yourname].  Open a bash terminal on your laptop, navigate to your Documents directory and execute the following commands to create a local version of your branch on your laptop:  
```
git clone https://github.com/15-16bayCS2/homework.git
cd homework
git branch yourname
git checkout yourname
git pull origin yourname
```
When there are new homework questions in master, or any other changes, e.g., to the README.md file, pull from master to your local branch, and push from your local branch to your branch on GitHub: 
```
git pull origin master
git push origin yourname
```
If you ...
```
cd ~/Documents/homework/cs61a/hw01
ls
```
... you will see a list of *.py files, one for each assigned question.  Open one for editing using, e.g.:
```
nano Q2.py
```
After you have made edits to Q2.py, push those edits from your local branch to your branch on GitHub :
```
git add -A
git commit -m "your commit message"
git push origin yourname
```
What could be simpler? ;)
