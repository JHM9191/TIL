### 1.1 

```bash
$ ls
$ touch 00_git_intro/Git.md
$ git status
$ git add .
$ git commit -m "added Git.md file"


student@M1305 MINGW64 ~/TIL (master)
$ ls
00_git_intro

student@M1305 MINGW64 ~/TIL (master)
$ touch 00_git_intro/Git.md
student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        00_git_intro/Git.md

nothing added to commit but untracked files present (use "git add" to track)

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master        
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   00_git_intro/Git.md


student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "added Git.md file"
[master 933b778] added Git.md file
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 00_git_intro/Git.md
```









### 1.2 log를 찍는 방법들

```bash
$ git log
$ git config --global --list
$ git log -2
$ git log --pretty=oneline
$ git log --oneline


student@M1305 MINGW64 ~/TIL (master)
$ git log
commit 933b77866739fc19a5774dad9324b8b2e1dbfc58 (HEAD -> master)
Author: JHM9191 <hm.jo.9191@gmail.com>
Date:   Tue Dec 10 10:21:50 2019 +0900

    added Git.md file

commit 65579e4cdce0c90aa06dd4f9a0026a9c8c54bc60 (origin/master)
Author: JHM9191 <hm.jo.9191@gmail.com>
Date:   Mon Dec 9 17:47:23 2019 +0900

    second commit

student@M1305 MINGW64 ~/TIL (master)
$ git config --global --list
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
user.name=JHM9191
user.email=hm.jo.9191@gmail.com

student@M1305 MINGW64 ~/TIL (master)
$ git log -2
commit 933b77866739fc19a5774dad9324b8b2e1dbfc58 (HEAD -> master)
Author: JHM9191 <hm.jo.9191@gmail.com>
Date:   Tue Dec 10 10:21:50 2019 +0900

    added Git.md file

commit 65579e4cdce0c90aa06dd4f9a0026a9c8c54bc60 (origin/master)
Author: JHM9191 <hm.jo.9191@gmail.com>
Date:   Mon Dec 9 17:47:23 2019 +0900

    second commit

$ git log --pretty=oneline
933b77866739fc19a5774dad9324b8b2e1dbfc58 (HEAD -> master) added Git.md file
65579e4cdce0c90aa06dd4f9a0026a9c8c54bc60 (origin/master) second commit
02946c0482ecfc35acb06fe9eefea771ba5b8b5d first commit

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
933b778 (HEAD -> master) added Git.md file
65579e4 (origin/master) second commit
02946c0 first commit
```





### 1.3 숨김 파일 만들기

```bash
student@M1305 MINGW64 ~/TIL (master)
$ touch .gitignore
```

> git이 직접 관리하지 않았으면 하는 파일이나 폴더를 만들곳 싶을때 `.`을 사용한다. 





##### 1.3.1 gitignore.io

> 보통 숨긴 파일이나 폴더를 하는 파일들 정리한 사이트
>
> 깃이 관리하지 않았으면 하는 파일이나 폴더. 
>
> 보통 git init을 한 후 바로 만든다. 





