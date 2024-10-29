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
  <a title="zh-CN" href="./GIT-USAGE_zh-CN.md">  <img src="https://img.shields.io/badge/-%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-545759?style=for-the-badge" alt="簡體中文"></a>
  <img src="https://img.shields.io/badge/-%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-A31F34?style=for-the-badge" alt="language">
</div>

![](./markdown-resource/git-c-ROV.png)
## Introduction of Git
我們將使用github和Git進行項目開發。
對於那些不知道如何使用Git的人，請訪問gitscm.com下載軟件（windows, mac, linux）並閲讀Pro Git小冊子。 </br>
你可以找到官方的pdf小冊子</br>
或者你可以閲讀項目的中文翻譯 (**建議**) </br>
或者你也可以在https://git-scm.com/book/en/v2上找到網頁版本，那裏提供了不同的語言。

請在我們下次會議前讀完中文版的**1 - 97頁和158 - 210頁**（~您也可以創建一個項目(repo)並嘗試一下）。

<div align="center">
<a title="zh-CN" href="./additional-resource/Git&Github_usage guidelines/Progit_V2.pdf"><img src="https://img.shields.io/badge/-Progit--english-545759?style=for-the-badge" alt="English" /></a>
<a title="zh-CN" href="./additional-resource/Git&Github_usage guidelines/Progit_V2_zh-CN.pdf"><img src="https://img.shields.io/badge/-progit--chinese簡體中文-A31F34?style=for-the-badge" alt="簡體中文"></a>
<a title="zh-CN" href="https://git-scm.com/book/en/v2"><img src="https://img.shields.io/badge/-progit--WEB VERSION-545759?style=for-the-badge" alt="簡體中文"></a>
</div>

> **Comments on different ways on using Git** </br>
> Jason Yang \<jiepengyang@outlook.com> </br>
> 雖然VS Code、GitHub Desktop或Git GUI等軟件提供了非常用户友好的界面和簡單易用的功能（真的很簡單），但這些軟件無法支持所有Git功能。這些應用程序可能無法執行某些複雜的操作（例如“git checkout HEAD~3”/“git pull --rebase”/“LF&CRLF轉換”），或者您可能會混淆相似的功能（例如，“合併”和“重置”有相似的中文翻譯）。</br>
因此，我建議您直接學習Git（一步到位，省時省力），不要害怕使用命令行，您很快就會習慣它的。

> **Short Abstract: WHAT IS GIT?**</br>
> Git 是一種分佈式版本控制系統，旨在以高速和高效的方式處理從小型項目到大型項目的一切事務。它允許多個開發人員同時在一個項目上工作，而不會覆蓋彼此的更改。Git 會記錄項目的更改歷史，促進團隊協作，並通過分支和合並來幫助管理項目版本。它在軟件開發中被廣泛用於跟蹤源代碼在軟件開發過程中的變化。

## ***Usage of Git*** (really important and useful)
在您閲讀了ProGit的必要部分之後，您可以學習以下部分。</br>
下面是一些使用Github和Git時要遵循的好習慣：
1. 每次在開始開發項目之前，你都應該**使用 Git 檢查遠程庫是否是最新的**，否則請拉取並將其變基到你自己的本地分支上。</br>  
**記住要使用 pull rebase 而不是 pull**，否則會產生一個無用的合併提交。如果其他人想查看倉庫的提交歷史，他們需要過濾掉這些垃圾和無用的合併提交，這會干擾其他人。</br>  
**記住在正確的分支上進行構建!!!** 在你進行 pull rebase 以保持與遠程倉庫的更新後，你可能會在不同的分支上。請切換回你自己的分支，然後繼續在項目上進行構建，***否則你的工作將無法保存!!!***
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
2. 每次在提交之前，**請確保將所有文件添加到緩存並進行一次良好的提交**。在你提交後，**檢查 Git 日誌以確保一切正確**，否則請進行修正並修改你的提交。最後將其推送到遠程（GitHub 倉庫）。*推送到遠程後，你可以選擇發起拉取請求以合併到 develop 或 main，或者繼續構建，但我建議你重新執行第一步，以確保一切正確*。
```
$ git status
--> If all up to date, continue your commit

$ git commit
$ git status
$ git log --pretty=oneline --graph --stat
--> Make sure you make a right commit

$ git push STEAM-ROV <your own remote branch, e.g., dev-JPYang>
```
3. 每次切換到另一個分支之前，**請先提交所有內容，否則你未保存的工作將被覆蓋!!!**  
```
$ git commit -a
$ git checkout <branch>
```
4. 每次在合併分支之前，**請確保你清楚地考慮想使用哪種方式：合併（快進）/ 變基**。如果在合併分支時遇到衝突且不確定如何修改，**請在羣組中詢問!!!**  
```
$ git merge <branch>
$ git rebase <branch>
```
## ***IMPORTANT & SERIOUSLY: Project's Regulation***
### Main Branch
1. 沒有人可以直接對其進行任何更新或修改。  
2. 主分支只接受拉取請求併合並develop分支。  
3. 必須在合併之前發起拉取請求，否則將被拒絕。  
4. 只有在develop分支中的所有內容經過測試並準備好發佈版本時，才能發起拉取請求並尋求合併批准。
### Develop branch
1. 所有內容必須合併或提交到此分支，才能發佈到主分支。
2. 只有熱修復或緊急問題可以直接對其進行任何更新或修改（但最好在單獨的分支上進行開發）。
3. 所有內容應在自己的develop分支上構建（例如，dev-JPYang，dev-Walter等）。 **避免多個貢獻者在同一分支上進行構建。這可以防止在推送到遠程時發生衝突**（這是一種不希望出現的情況，雖然可以通過 `git pull --rebase` 解決，但會有些困難並且容易出錯）。
### Dev-\<Contributor> Branch
1. 每位貢獻者應創建自己的分支。
2. 每個分支只允許一個貢獻者，以防止推送衝突！
### Special files or folders
***以下是項目中的特殊文件或文件夾***</br>
按字母順序列出（從A到Z）

| Items                                            |  Type  |
| ------------------------------------------------ | :----: |
| ./.gitignore                                     |  file  |
| ./markdown-resource/cover-ROV.png                |  file  |
| ./markdown-resource/.+-c-ROV\.png$               | files  |
| ./additional-resource/Git&Github_usage guidlines | folder |
| ./markdown-resource/fontawesome/                 | folder |
| ./markdown-resource/webfonts/                    | folder |
- 如果您想對其進行任何修改，必須尋求他人的批准並提供合理的解釋。
- 對這些特殊文件或文件夾的修改應創建單獨的提交。
- 特殊文件的修改應直接在develop分支上進行，所有其他貢獻者應立即從遠程存儲進行拉取重基。
---
#### Contributor of git usage and regulation
**Jason Yang \<jiepengyang@outlook.com>**