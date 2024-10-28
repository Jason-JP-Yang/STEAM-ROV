# ROV Project - ***GIT USAGE AND REGULATION***
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/all.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/fontawesome.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/brands.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/solid.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/regular.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/thin.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/light.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/duotone.min.css">
<link rel="stylesheet" type="text/css" href="./markdown-resource/fontawesome/sharp-solid.min.css">

> Hong Kong Po Leung Kuk Ngan Po Ling College Steam Team Robotics ROV Team 2 </br>
> Teammates: JP-YANG, Jasmine, Walter, Mark Chan, Kasey Chan
<div align="right">
<img src="https://img.shields.io/badge/-English-A31F34?style=for-the-badge" alt="English" />
<a title="zh-CN" href="README_zh-CN.md"><img src="https://img.shields.io/badge/-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-545759?style=for-the-badge" alt="简体中文"></a>
<a title="zh-TW" href="README_zh-TW.md"><img src="https://img.shields.io/badge/-%E7%B9%81%E4%BD%93%E4%B8%AD%E6%96%87-545759?style=for-the-badge" alt="繁体中文"></a>
</div>  

![](./markdown-resource/git-c-ROV.png)
## Introduction of Git
We will use github and Git for our project development.
For those who don't know how to use Git, please visit git-scm.com to download software (window, mac, linux) and read the Pro Git Booklet. </br>
You can find the official pdf booklet</br>
Or you can read the chinese translation of progit (**suggested**) </br>
Or you can also find web version at https://git-scm.com/book/en/v2, there are different languages provided.

Please finish reading of **Page 1 - 97 & Page 158 - 210** of the booklet in chinese version before our next meeting (~you can also create a repo and have some try).

<div align="center">
<a title="zh-CN" href="./additional-resource/Git&Github_usage guidelines/Progit_V2.pdf"><img src="https://img.shields.io/badge/-Progit--english-545759?style=for-the-badge" alt="English" /></a>
<a title="zh-CN" href="./additional-resource/Git&Github_usage guidelines/Progit_V2_zh-CN.pdf"><img src="https://img.shields.io/badge/-progit--chinese简体中文-A31F34?style=for-the-badge" alt="简体中文"></a>
<a title="zh-CN" href="https://git-scm.com/book/en/v2"><img src="https://img.shields.io/badge/-progit--WEB VERSION-545759?style=for-the-badge" alt="简体中文"></a>
</div>

> **Comments on different ways on using Git** </br>
> Jason Yang \<jiepengyang@outlook.com> </br>
> Although VS-Code or Github Desktop or Git GUI etc. provide very user-friendly interface and simple and easy to use (really simple), these software cannot support all git functions. Some difficult actions these app cannot carry out (git checkout HEAD~3 / git pull --rebase / LF&CRLF convert) or you may easily mix similar functions up (e.g., merge / rebase have similar chinese translation) </br>
Therefore, i suggest you can study Git directly (一步到位 省时省力), don't afraid of using command line, you will get used to it after a while

> **Short Abstract: WHAT IS GIT?**</br>
> Git is a distributed version control system designed to handle everything from small to very large projects with speed and efficiency. It allows multiple developers to work on a project simultaneously without overwriting each other’s changes. Git keeps a history of changes, facilitates collaboration, and helps manage project versions through branching and merging. It is widely used in software development for tracking changes in source code during software development.

## ***Usage of Git*** (really important and useful)
After you have read the necessary parts of ProGit you can learn about the following sections. </br>
Here are some good habits to follow when using Github and Git:
1. Every time before you start to develop your project you show **use git to check everything is up to date on remote** otherwise pull and rebase to your own local branches. </br> 
**Remember to use pull rebase instead of pull**, otherwise there will produce a useless merge commit. If other people want to check the history of commits of repo, they need to filter out these rubbish and useless merge commits which disturb others. 
``` 
$ git remote show <remote repo, e.g., STEAM-ROV>

## Example return:
* remote STEAM-ROV
  Fetch URL: https://github.com/Jason-JP-Yang/STEAM-ROV.git
  Push  URL: https://github.com/Jason-JP-Yang/STEAM-ROV.git
  HEAD branch: main
  Remote branches:
    dev-JPYang tracked
    develop    tracked
    main       tracked
  Local refs configured for 'git push':
    dev-JPYang pushes to dev-JPYang (up to date)
    develop    pushes to develop    (up to date)
    main       pushes to main       (not up to date)

$ git checkout main
$ git pull STEAM-ROV main --rebase
```
2. Every time before you make a commit, **please make sure you add all files to cache and make a good commit**. After you made a commit, **check the git log to ensure everything is correct** otherwise make correction and amend your commit. Finally push it to the remote (Github repo). *After push to the remote you can either make a pull reuqest to merge to develop or main or continue your building but i suggest to redo the first step again make sure everything correct*
```
$ git status
--> If all up to date, continue your commit

$ git commit
$ git status
$ git log --pretty=oneline --graph --stat
--> Make sure you make a right commit

$ git push STEAM-ROV <your own remote branch, e.g., dev-JPYang>
```
3. Every time you checkout to another branch, **please commit everything first, otherwise all your unsaved work will be overwrite!!!**
```
$ git commit -a
$ git checkout <branch>
```

4. Every time before you merge a branch, **please make sure you think clearly which mode you want to use: MERGE (fast-forward) / REBASE**. If you face conflict during merge branches and not sure how to amend, **PLEASE ASK AT GROUP!!!**
```
$ git merge <branch>
$ git rebase <branch>
```
## ***IMPORTANT & SERIOUSLY: Branch Regulation***
### Main Branch
1. NO ONE can directly make any updates or modify anything on it.
2. MAIN BRANCH only accept pull request and merge DEVELOP branch.
3. Pull request before merge otherwise will be rejected.
4. Only when everything in develop branched is tested and ready to publish a version, then can make a pull request and seek approval to merge.
### Develop branch
1. Everything must merge or submit to this branch before publish to main branch.
2. Only hotfix or emergency issue can directly make any updates or modify anything on it (but better develop on a separate branch).
3. Everything should be build on your own dev-branch (e.g., dev-JPYang, dev-Walter, etc.). **Avoid more than one contributors build on the same branch. This prevent conflicts happened during push to remote** (It is a unwanted situations, although it can solve by `git pull --rebase` but little difficult and easily make error).
### Dev-\<Contributor> Branch
1. Every contributor should create his / her own branch
2. Only one contributor is allowed in each branch in order to prevent push conflicts!