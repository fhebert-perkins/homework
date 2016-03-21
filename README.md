# homework
This is where homework assignments will be posted and submitted.

Please submit your code for Questions 2, 4, 5 and 6.  Question 7 is optional.  Due 3/21/2016 12:40pm
# How to use git
```
git clone https://github.com/15-16bayCS2/homework.git
cd homework
git branch yourname
git checkout yourname
git pull origin yourname
```
When there are new homework questions in master, or any other changes, e.g., to the README.md file, first make sure you are in your local branch:
```
git checkout yourname
```
Then pull from master to your local branch, and push from your local branch to your branch on GitHub: 
```
git pull origin master
git push origin yourname
```
After you have made edits to your work, push those edits from your local branch to your branch on GitHub :
```
git add -A
git commit -m "your commit message"
git push origin yourname
```
