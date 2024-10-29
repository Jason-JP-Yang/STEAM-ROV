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
  <a title="en" href="./GIT-USAGE.md"><img src="https://img.shields.io/badge/-English-545759?style=for-the-badge" alt="english"></a>
  <img src="https://img.shields.io/badge/-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-A31F34?style=for-the-badge" alt="简体中文">
  <a title="zh-TW" href="./GIT-USAGE_zh-TW.md"><img src="https://img.shields.io/badge/-%E7%B9%81%E4%BD%93%E4%B8%AD%E6%96%87-545759?style=for-the-badge" alt="繁体中文"></a>
</div>

![](./markdown-resource/git-c-ROV.png)
## Introduction of Git
我们将使用github和Git进行项目开发。
对于那些不知道如何使用Git的人，请访问gitscm.com下载软件（windows, mac, linux）并阅读Pro Git小册子。 </br>
你可以找到官方的pdf小册子</br>
或者你可以阅读项目的中文翻译 (**建议**) </br>
或者你也可以在https://git-scm.com/book/en/v2上找到网页版本，那里提供了不同的语言。

请在我们下次会议前读完中文版的**1 - 97页和158 - 210页**（~您也可以创建一个项目(repo)并尝试一下）。

<div align="center">
<a title="zh-CN" href="./additional-resource/Git&Github_usage guidelines/Progit_V2.pdf"><img src="https://img.shields.io/badge/-Progit--english-545759?style=for-the-badge" alt="English" /></a>
<a title="zh-CN" href="./additional-resource/Git&Github_usage guidelines/Progit_V2_zh-CN.pdf"><img src="https://img.shields.io/badge/-progit--chinese简体中文-A31F34?style=for-the-badge" alt="简体中文"></a>
<a title="zh-CN" href="https://git-scm.com/book/en/v2"><img src="https://img.shields.io/badge/-progit--WEB VERSION-545759?style=for-the-badge" alt="简体中文"></a>
</div>

> **Comments on different ways on using Git** </br>
> Jason Yang \<jiepengyang@outlook.com> </br>
> 虽然VS Code、GitHub Desktop或Git GUI等软件提供了非常用户友好的界面和简单易用的功能（真的很简单），但这些软件无法支持所有Git功能。这些应用程序可能无法执行某些复杂的操作（例如“git checkout HEAD~3”/“git pull --rebase”/“LF&CRLF转换”），或者您可能会混淆相似的功能（例如，“合并”和“重置”有相似的中文翻译）。</br>
因此，我建议您直接学习Git（一步到位，省时省力），不要害怕使用命令行，您很快就会习惯它的。

> **Short Abstract: WHAT IS GIT?**</br>
> Git 是一种分布式版本控制系统，旨在以高速和高效的方式处理从小型项目到大型项目的一切事务。它允许多个开发人员同时在一个项目上工作，而不会覆盖彼此的更改。Git 会记录项目的更改历史，促进团队协作，并通过分支和合并来帮助管理项目版本。它在软件开发中被广泛用于跟踪源代码在软件开发过程中的变化。

## ***Usage of Git*** (really important and useful)
在您阅读了ProGit的必要部分之后，您可以学习以下部分。</br>
下面是一些使用Github和Git时要遵循的好习惯：
1. 每次在开始开发项目之前，你都应该**使用 Git 检查远程库是否是最新的**，否则请拉取并将其变基到你自己的本地分支上。</br>  
**记住要使用 pull rebase 而不是 pull**，否则会产生一个无用的合并提交。如果其他人想查看仓库的提交历史，他们需要过滤掉这些垃圾和无用的合并提交，这会干扰其他人。</br>  
**记住在正确的分支上进行构建!!!** 在你进行 pull rebase 以保持与远程仓库的更新后，你可能会在不同的分支上。请切换回你自己的分支，然后继续在项目上进行构建，***否则你的工作将无法保存!!!***
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

$ (git config alias.co checkout)
$ git co (checkout) <branch>
```
2. 每次在提交之前，**请确保将所有文件添加到缓存并进行一次良好的提交**。在你提交后，**检查 Git 日志以确保一切正确**，否则请进行修正并修改你的提交。最后将其推送到远程（GitHub 仓库）。*推送到远程后，你可以选择发起拉取请求以合并到 develop 或 main，或者继续构建，但我建议你重新执行第一步，以确保一切正确*。
```
$ git status
--> If all up to date, continue your commit

$ git commit
$ git status
$ git log --pretty=oneline --graph --stat
--> Make sure you make a right commit

$ git push STEAM-ROV <your own remote branch, e.g., dev-JPYang>
```
3. 每次切换到另一个分支之前，**请先提交所有内容，否则你未保存的工作将被覆盖!!!**  
```
$ git commit -a
$ git checkout <branch>
```
4. 每次在合并分支之前，**请确保你清楚地考虑想使用哪种方式：合并（快进）/ 变基**。如果在合并分支时遇到冲突且不确定如何修改，**请在群组中询问!!!**  
```
$ git merge <branch>
$ git rebase <branch>
```
## ***IMPORTANT & SERIOUSLY: Branch Regulation***
### Main Branch
1. 没有人可以直接对其进行任何更新或修改。  
2. 主分支只接受拉取请求并合并develop分支。  
3. 必须在合并之前发起拉取请求，否则将被拒绝。  
4. 只有在develop分支中的所有内容经过测试并准备好发布版本时，才能发起拉取请求并寻求合并批准。
### Develop branch
1. 所有内容必须合并或提交到此分支，才能发布到主分支。
2. 只有热修复或紧急问题可以直接对其进行任何更新或修改（但最好在单独的分支上进行开发）。
3. 所有内容应在自己的develop分支上构建（例如，dev-JPYang，dev-Walter等）。 **避免多个贡献者在同一分支上进行构建。这可以防止在推送到远程时发生冲突**（这是一种不希望出现的情况，虽然可以通过 `git pull --rebase` 解决，但会有些困难并且容易出错）。
### Dev-\<Contributor> Branch
1. 每位贡献者应创建自己的分支。
2. 每个分支只允许一个贡献者，以防止推送冲突！
### Special files or folders
***以下是项目中的特殊文件或文件夹***</br>
按字母顺序列出（从A到Z）

| Items                                            |  Type  |
| ------------------------------------------------ | :----: |
| ./.gitignore                                     |  file  |
| ./markdown-resource/cover-ROV.png                |  file  |
| ./markdown-resource/.+-c-ROV\.png$               | files  |
| ./additional-resource/Git&Github_usage guidlines | folder |
| ./markdown-resource/fontawesome/                 | folder |
| ./markdown-resource/webfonts/                    | folder |
- 如果您想对其进行任何修改，必须寻求他人的批准并提供合理的解释。
- 对这些特殊文件或文件夹的修改应创建单独的提交。
- 特殊文件的修改应直接在develop分支上进行，所有其他贡献者应立即从远程存储进行拉取重基。
---
#### Contributor of git usage and regulation
**Jason Yang \<jiepengyang@outlook.com>**