로컬과 리모트로 나뉜다. 

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
>
> .gitignore 깃이 관리하는 것을 무시하게 만든다. 
>
> 어떤파일들이 있을까?

- .vscode 처럼 세팅과 관련된 파일들은 git으로 관리하는 것이 의미가 없음. 
- 키값과 같은 데이터는 gitignore에 넣어줘야함. 
  - github에서 이러한 키값을 찾아서 탈취하는 사람들이 있음. 





##### 1.3.1 gitignore.io

> 보통 숨긴 파일이나 폴더를 하는 파일들 정리한 사이트
>
> 깃이 관리하지 않았으면 하는 파일이나 폴더. 
>
> 보통 git init을 한 후 바로 만든다. 
>
> http://gitignore.io/





```bash
student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        00_git_intro/todaygit.md

nothing added to commit but untracked files present (use "git add" to track)

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)  
        new file:   .gitignore
        new file:   00_git_intro/todaygit.md


student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "added .gitignore file"
[master 7044b09] added .gitignore file
 2 files changed, 249 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
7044b09 (HEAD -> master) added .gitignore file
933b778 added Git.md file
65579e4 (origin/master) second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 11, done.
Counting objects: 100% (11/11), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (9/9), 2.51 KiB | 1.26 MiB/s, done.
Total 9 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To https://github.com/JHM9191/TIL.git
   65579e4..7044b09  master -> master

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
7044b09 (HEAD -> master, origin/master) added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit
```







### 1.4 README.md

>repository를 소개하는 파일.
>
>directory에 왔을 때 제일 먼저 보는 파일.



```bash
student@M1305 MINGW64 ~/TIL (master)
$ touch README.md
```









merge conflict

Auto merge





- 빔창이 나온 경우:
  - `ESC` 5번
  - :wq
  - i( 수정할 때 사용함.)



숨긴 폴더 보기

```
ls -a
```



### 1.5 reset



```bash
# add 완전 전 상태로 
# 더이상 git이 관리하지 않겠다는 의미. 
$ git rm --cached 01_git_reset/reset2.txt



# reset을 사용하면 원래 상태로 돌릴 수 있음.
$ git reset HEAD 01_git_reset/reset.txt



```



![image-20191210152133986](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210152133986.png)



```bash
.gitignore에 

reset2.txt를 추가하는 경우엔 git이 더이상 관리하지 않게 됨.
```



![image-20191210152328284](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210152328284.png)





```bash
$ git add 01_git_reset/reset.txt
$ git commit -m "added reset.txt files"

```





![image-20191210152417239](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210152417239.png)







```bash
$ git commit --amend
```





### commit할 때 같이 commit해야할 파일을 빠트린 경우



```bash
$ git commit --amend
```





### Git Flow

> master 가 메인임. 



- 마스터가 메임
  - 배포된 프로그램들은 모두 마스터임. 
- develop branch
  - feature branch
- halffix
  - 취합한 후 버그가 있어서 수정을 해야할 경우 사용해야함. 







### Making Branches



```bash
$ git branch feature/test

$ git branch
  feature/test
* master

# branch로 이동
$ git checkout feature/test 

# 결과
Switched to branch 'feature/test'
M       00_git_intro/todaygit.md

# master로 다시 나오기
$ git checkout master 

# branch 삭제 (merging이 이루어진 branch를 삭제할 때 사용됨.)
$ git branch --d feature/test 

# 결과
Deleted branch feature/test (was 35557ad).

#
$ git branch
* master

# branch 생성과 동시에 이동.
$ git checkout -b feacher/test

# branch를 강제로 삭제. (merging을 하지 않은 상태에서 삭제할 때 사용됨.)
$ git branch -D feacher/test 




```





```bash
student@M1305 MINGW64 ~/TIL (master)
$ git checkout -b feature/test
Switched to a new branch 'feature/test'

student@M1305 MINGW64 ~/TIL (feature/test)
$ touch 02_git_branch/merge-test.txt



```


- git에 있는 특수한 포인터
- 가장 최신의 경로?



![image-20191210160649993](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210160649993.png)

![image-20191210160658080](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210160658080.png)















- git에 있는 특수한 포인터
- 가장 최근에 위치하고 있는  위치. 



```bash

student@M1305 MINGW64 ~/TIL/00_git_intro (master)
$ touch reset.txt reset2.txt

student@M1305 MINGW64 ~/TIL/00_git_intro (master)
$ cd ..

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   00_git_intro/todaygit.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        00_git_intro/reset.txt
        00_git_intro/reset2.txt
        README.md

no changes added to commit (use "git add" and/or "git commit -a")

student@M1305 MINGW64 ~/TIL (master)
$ mkdir 01_git_reset

student@M1305 MINGW64 ~/TIL (master)
$ cd 01_git_reset/

student@M1305 MINGW64 ~/TIL/01_git_reset (master)
$ touch reset.txt reset2.txt

student@M1305 MINGW64 ~/TIL/01_git_reset (master)
$ cd ..

student@M1305 MINGW64 ~/TIL (master)
$ git reset HEAD 01_git_reset/reset.txt
Unstaged changes after reset:
M       00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git rm --cashed 01_git_reset/reset2.txt
error: unknown option `cashed'
usage: git rm [<options>] [--] <file>...

    -n, --dry-run         dry run
    -q, --quiet           do not list removed files
    --cached              only remove from the index
    -f, --force           override the up-to-date check
    -r                    allow recursive removal
    --ignore-unmatch      exit with a zero status even if nothing matched


student@M1305 MINGW64 ~/TIL (master)
$ rm
rm: missing operand
Try 'rm --help' for more information.

student@M1305 MINGW64 ~/TIL (master)
$ rm --cached
rm: unknown option -- cached
Try 'rm --help' for more information.

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   00_git_intro/reset.txt
        new file:   00_git_intro/reset2.txt
        modified:   00_git_intro/todaygit.md
        new file:   01_git_reset/reset.txt
        new file:   01_git_reset/reset2.txt
        new file:   README.md


student@M1305 MINGW64 ~/TIL (master)
$ git rm --cached 01_git_reset/reset2.txt
rm '01_git_reset/reset2.txt'

student@M1305 MINGW64 ~/TIL (master)
$ get add .
bash: get: command not found

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   00_git_intro/reset.txt
        new file:   00_git_intro/reset2.txt
        modified:   00_git_intro/todaygit.md
        new file:   01_git_reset/reset.txt
        new file:   01_git_reset/reset2.txt
        new file:   README.md


student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "Added reset.txt and reset2.txt"
[master c8a4402] Added reset.txt and reset2.txt
 6 files changed, 424 insertions(+)
 create mode 100644 00_git_intro/reset.txt
 create mode 100644 00_git_intro/reset2.txt
 create mode 100644 01_git_reset/reset.txt
 create mode 100644 01_git_reset/reset2.txt
 create mode 100644 README.md

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   01_git_reset/reset.txt
        modified:   01_git_reset/reset2.txt


student@M1305 MINGW64 ~/TIL (master)
$ git reset HEAD 01_git_reset/reset.txt
Unstaged changes after reset:
M       01_git_reset/reset.txt

student@M1305 MINGW64 ~/TIL (master)
$ git rm --cached 01_git_reset/reset2.txt
rm '01_git_reset/reset2.txt'

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    01_git_reset/reset2.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   01_git_reset/reset.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        01_git_reset/reset2.txt


student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    01_git_reset/reset2.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   00_git_intro/todaygit.md
        modified:   01_git_reset/reset.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)       
        01_git_reset/reset2.txt

added reset.txt files
added reset.txt files

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    01_git_reset/reset2.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   00_git_intro/todaygit.md
        modified:   01_git_reset/reset.txt


student@M1305 MINGW64 ~/TIL (master)
$ git add 01_git_reset/reset.txt

added reset.txt 
student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "added reset.txt files"
[master 6118aee] added reset.txt files
 2 files changed, 1 insertion(+)
 delete mode 100644 01_git_reset/reset2.txt

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
6118aee (HEAD -> master) added reset.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 (origin/master) added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git add .gitignore

student@M1305 MINGW64 ~/TIL (master)
$ git commit --amend
[master 5ba4fd6] added reset.txt files
 Date: Tue Dec 10 15:24:01 2019 +0900
added reset.txt and omit_file.txt files
 3 files changed, 3 insertions(+)
 delete mode 100644 01_git_reset/reset2.txt

student@M1305 MINGW64 ~/TIL (master)
$ git commit --amend
[master b1676ac] added reset.txt files
 Date: Tue Dec 10 15:24:01 2019 +0900
 3 files changed, 3 insertions(+)
 delete mode 100644 01_git_reset/reset2.txt

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
b1676ac (HEAD -> master) added reset.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 (origin/master) added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ ls
00_git_intro  01_git_reset  README.md

student@M1305 MINGW64 ~/TIL (master)
$ git commit --amend
[master 76c897b] added reset.txt
 Date: Tue Dec 10 15:24:01 2019 +0900
 3 files changed, 3 insertions(+)
 delete mode 100644 01_git_reset/reset2.txt

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
76c897b (HEAD -> master) added reset.txt
c8a4402 Added reset.txt and reset2.txt
7044b09 (origin/master) added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ touch 01_git_reset/omit_file.txt

student@M1305 MINGW64 ~/TIL (master)
$ git add 01_git_reset/omit_file.txt

student@M1305 MINGW64 ~/TIL (master)
$ git commit --amend
[master ede9fb5] added reset.txt and omit_file.txt files
 Date: Tue Dec 10 15:24:01 2019 +0900
 3 files changed, 3 insertions(+)
 rename 01_git_reset/{reset2.txt => omit_file.txt} (100%)

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
ede9fb5 (HEAD -> master) added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 (origin/master) added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "updated .gitignore"
On branch master
Changes not staged for commit:
        deleted:    00_git_intro/reset.txt
        deleted:    00_git_intro/reset2.txt
        modified:   00_git_intro/todaygit.md

no changes added to commit

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "updated .gitignore"
[master 35557ad] updated .gitignore
 3 files changed, 67 insertions(+), 5 deletions(-)
 delete mode 100644 00_git_intro/reset.txt
 delete mode 100644 00_git_intro/reset2.txt

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
nothing to commit, working tree clean

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
35557ad (HEAD -> master) updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 (origin/master) added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 19, done.
Counting objects: 100% (19/19), done.
Delta compression using up to 8 threads
Compressing objects: 100% (14/14), done.
Writing objects: 100% (15/15), 5.60 KiB | 1.87 MiB/s, done.
Total 15 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 2 local objects.
To https://github.com/JHM9191/TIL.git
   7044b09..35557ad  master -> master

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
35557ad (HEAD -> master, origin/master) updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ ls
00_git_intro  01_git_reset  README.md

student@M1305 MINGW64 ~/TIL (master)
$ mkdir 02_git_branch

student@M1305 MINGW64 ~/TIL (master)
$ ls
00_git_intro  01_git_reset  02_git_branch  README.md

student@M1305 MINGW64 ~/TIL (master)
$ git branch feature/test

student@M1305 MINGW64 ~/TIL (master)
$ git branch
  feature/test
* master

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test 
Switched to branch 'feature/test'
M       00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL (feature/test)
$ git checkout master 
Switched to branch 'master'
M       00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL (master)
$ git branch --d feature/test 
Deleted branch feature/test (was 35557ad).

student@M1305 MINGW64 ~/TIL (master)
$ git branch
* master

student@M1305 MINGW64 ~/TIL (master)
$ git checkout -b feacher/test
Switched to a new branch 'feacher/test'

student@M1305 MINGW64 ~/TIL (feacher/test)
$ git checkout master
Switched to branch 'master'
M       00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL (master)
$ git checkout --d feacher/test 
HEAD is now at 35557ad updated .gitignore
M       00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL ((35557ad...))
$ git checkout master
Switched to branch 'master'
M       00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   00_git_intro/todaygit.md

no changes added to commit (use "git add" and/or "git commit -a")

student@M1305 MINGW64 ~/TIL (master)
$ git branch
  feacher/test
* master

student@M1305 MINGW64 ~/TIL (master)
$ git checkout -D feacher/test 
error: unknown switch `D'
usage: git checkout [<options>] <branch>
   or: git checkout [<options>] [<branch>] -- <file>...

    -b <branch>           create and checkout a new branch
    -B <branch>           create/reset and checkout a branch
    -l                    create reflog for new branch
    --overlay             use overlay mode (default)
    -q, --quiet           suppress progress reporting
    --recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --progress            force progress reporting
    -m, --merge           perform a 3-way merge with the new branch
    --conflict <style>    conflict style (merge or diff3)
    -d, --detach          detach HEAD at named commit
    -t, --track           set upstream info for new branch
    -f, --force           force checkout (throw away local modifications)
    --orphan <new-branch>
                          new unparented branch
    --overwrite-ignore    update ignored files (default)
    --ignore-other-worktrees
                          do not check if another worktree is holding the given ref
    -2, --ours            checkout our version for unmerged files
    -3, --theirs          checkout their version for unmerged files
    -p, --patch           select hunks interactively
    --ignore-skip-worktree-bits
                          do not limit pathspecs to sparse entries only


student@M1305 MINGW64 ~/TIL (master)
$ git branch -D feacher/test
Deleted branch feacher/test (was 35557ad).

student@M1305 MINGW64 ~/TIL (master)
$ git checkout -b feature/test
Switched to a new branch 'feature/test'

student@M1305 MINGW64 ~/TIL (feature/test)
$ touch 02_git_branch/merge-test.txt

student@M1305 MINGW64 ~/TIL (feature/test)
$
$ git add .

student@M1305 MINGW64 ~/TIL (feature/test)
$ git commit -m "added merge-test.txt"
[feature/test 97970bd] added merge-test.txt
 2 files changed, 93 insertions(+)
 create mode 100644 02_git_branch/merge-test.txt

student@M1305 MINGW64 ~/TIL (feature/test)
$ git log --oneline
97970bd (HEAD -> feature/test) added merge-test.txt
35557ad (origin/master, master) updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (feature/test)
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test 
error: Your local changes to the following files would be overwritten by checkout:
        00_git_intro/todaygit.md
Please commit your changes or stash them before you switch branches.
Aborting

student@M1305 MINGW64 ~/TIL (master)
$ git checkout master
Already on 'master'
M       00_git_intro/todaygit.md

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test 
error: Your local changes to the following files would be overwritten by checkout:
        00_git_intro/todaygit.md
Please commit your changes or stash them before you switch branches.
error: The following untracked working tree files would be overwritten by checkout:
        02_git_branch/merge-test.txt
Please move or remove them before you switch branches.
Aborting

student@M1305 MINGW64 ~/TIL (master)
$ git merge feature/test 
error: Your local changes to the following files would be overwritten by merge:
        00_git_intro/todaygit.md
Please commit your changes or stash them before you merge.
error: The following untracked working tree files would be overwritten by merge:
        02_git_branch/merge-test.txt
Please move or remove them before you merge.
Aborting
Updating 35557ad..97970bd

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test 
error: Your local changes to the following files would be overwritten by checkout:
        00_git_intro/todaygit.md
Please commit your changes or stash them before you switch branches.
error: The following untracked working tree files would be overwritten by checkout:
        02_git_branch/merge-test.txt
Please move or remove them before you switch branches.
Aborting

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
35557ad (HEAD -> master, origin/master) updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git branch
  feature/test
* master

student@M1305 MINGW64 ~/TIL (master)
$ git branch --d feature/test 
error: The branch 'feature/test' is not fully merged.
If you are sure you want to delete it, run 'git branch -D feature/test'.

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test 
error: Your local changes to the following files would be overwritten by checkout:
        00_git_intro/todaygit.md
        02_git_branch/merge-test.txt
Please commit your changes or stash them before you switch branches.
Aborting

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test 
error: Your local changes to the following files would be overwritten by checkout:
        00_git_intro/todaygit.md
        02_git_branch/merge-test.txt
Please commit your changes or stash them before you switch branches.
Aborting

student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "commit"
[master 41f9e38] commit
 2 files changed, 97 insertions(+)
Merge branch 'feature/test'
 create mode 100644 02_git_branch/me

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test
Switched to branch 'feature/test'

student@M1305 MINGW64 ~/TIL (feature
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git merge feature/test
CONFLICT (add/add): Merge conflict i
Auto-merging 02_git_branch/merge-tes
Auto-merging 00_git_intro/todaygit.m
CONFLICT (content): Merge conflict i
Automatic merge failed; fix conflict

student@M1305 MINGW64 ~/TIL (master|
$ git add .

student@M1305 MINGW64 ~/TIL (master|
$ git merge feature/test
fatal: You have not concluded your m
Please, commit your changes before y

student@M1305 MINGW64 ~/TIL (master|
$ git checkout feature/test
error: Your local changes to the fol
        00_git_intro/todaygit.md
Please commit your changes or stash
Aborting

student@M1305 MINGW64 ~/TIL (master|
$ git commit
[master ace5fe1] Merge branch 'feature/test'

student@M1305 MINGW64 ~/TIL (master)
$ git merge feature/test 
Already up to date.

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/test 
Switched to branch 'feature/test'

student@M1305 MINGW64 ~/TIL (feature/test)
$ git commit -m "merge-test.txt changed"
On branch feature/test
Changes not staged for commit:
        modified:   02_git_branch/merge-test.txt

no changes added to commit

student@M1305 MINGW64 ~/TIL (feature/test)
$ git checkout master
error: Your local changes to the following files would be overwritten by checkout:
        02_git_branch/merge-test.txt
Please commit your changes or stash them before you switch branches.
Aborting

student@M1305 MINGW64 ~/TIL (feature/test)
$ git merge feature/test 
Already up to date.

student@M1305 MINGW64 ~/TIL (feature/test)
$ git checkout -b feature/test
fatal: A branch named 'feature/test' already exists.

student@M1305 MINGW64 ~/TIL (feature/test)
$ git checkout -b feature/test2
Switched to a new branch 'feature/test2'

student@M1305 MINGW64 ~/TIL (feature/test2)
$ touch 02_git_branch/test.html

student@M1305 MINGW64 ~/TIL (feature/test2)
$ git status
On branch feature/test2
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   00_git_intro/todaygit.md
        modified:   02_git_branch/merge-test.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        02_git_branch/test.html

no changes added to commit (use "git add" and/or "git commit -a")

student@M1305 MINGW64 ~/TIL (feature/test2)
$ git add .

student@M1305 MINGW64 ~/TIL (feature/test2)
$ git status
On branch feature/test2
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   00_git_intro/todaygit.md
        modified:   02_git_branch/merge-test.txt
        new file:   02_git_branch/test.html


student@M1305 MINGW64 ~/TIL (feature/test2)
$ git commit -m "Complete test.html"
[feature/test2 67d2a3f] Complete test.html
 3 files changed, 26 insertions(+)
 create mode 100644 02_git_branch/test.html

student@M1305 MINGW64 ~/TIL (feature/test2)
$ git log --oneline
67d2a3f (HEAD -> feature/test2) Complete test.html
97970bd (feature/test) added merge-test.txt       
35557ad (origin/master) updated .gitignore        
ede9fb5 added reset.txt and omit_file.txt files   
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (feature/test2)
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
ace5fe1 (HEAD -> master) Merge branch 'feature/test'
41f9e38 commit
97970bd (feature/test) added merge-test.txt
35557ad (origin/master) updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git merge feature/test2
Auto-merging 02_git_branch/merge-test.txt
CONFLICT (content): Merge conflict in 02_git_branch/merge-test.txt
Auto-merging 00_git_intro/todaygit.md
CONFLICT (content): Merge conflict in 00_git_intro/todaygit.md
Automatic merge failed; fix conflicts and then commit the result.

student@M1305 MINGW64 ~/TIL (master|MERGING)
$ git log --oneline
ace5fe1 (HEAD -> master) Merge branch 'feature/test'
41f9e38 commit
97970bd (feature/test) added merge-test.txt
35557ad (origin/master) updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master|MERGING)
$ git branch --d feature/test2
error: The branch 'feature/test2' is not fully merged.
If you are sure you want to delete it, run 'git branch -D feature/test2'.

student@M1305 MINGW64 ~/TIL (master|MERGING)
$ git push origin master
Enumerating objects: 17, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 8 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (14/14), 1.77 KiB | 905.00 KiB/s, done.
remote: Resolving deltas: 100% (9/9), completed with 2 local objects.
To https://github.com/JHM9191/TIL.git
   35557ad..ace5fe1  master -> master

student@M1305 MINGW64 ~/TIL (master|MERGING)
$ s
bash: s: command not found

student@M1305 MINGW64 ~/TIL (master|MERGING)
$ git log --oneline
ace5fe1 (HEAD -> master, origin/master) Merge branch 'feature/test'
41f9e38 commit
97970bd (feature/test) added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master|MERGING)
$
$ git branch
  feature/test
  feature/test2
* master

student@M1305 MINGW64 ~/TIL (master|MERGING)
$ git status
On branch master
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Changes to be committed:
        new file:   02_git_branch/test.html

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   00_git_intro/todaygit.md
        both modified:   02_git_branch/merge-test.txt


student@M1305 MINGW64 ~/TIL (master|MERGING)
$ git add .

student@M1305 MINGW64 ~/TIL (master|MERGING)
$ git commit -m "completed merge"
[master 7b7e648] completed merge

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
7b7e648 (HEAD -> master) completed merge
67d2a3f (feature/test2) Complete test.html
ace5fe1 (origin/master) Merge branch 'feature/test'
41f9e38 commit
97970bd (feature/test) added merge-test.txt

student@M1305 MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 22, done.
Counting objects: 100% (22/22), done.  
Delta compression using up to 8 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (12/12), 1.05 KiB | 537.00 KiB/s, done.
Total 12 (delta 6), reused 0 (delta 0)
remote: Resolving deltas: 100% (6/6), completed with 3 local objects.
To https://github.com/JHM9191/TIL.git
   ace5fe1..7b7e648  master -> master

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
7b7e648 (HEAD -> master, origin/master) completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files        
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git checkout -b feature/signup
Switched to a new branch 'feature/signup'

student@M1305 MINGW64 ~/TIL (feature/signup)
$ touch 02_git_branch/signup.html

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git status
On branch feature/signup
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        02_git_branch/signup.html

nothing added to commit but untracked files present (use "git add" to track)

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git add .

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git status
On branch feature/signup
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   02_git_branch/signup.html


student@M1305 MINGW64 ~/TIL (feature/signup)
$ git commit -m "Complete signup.html"
[feature/signup 2d928ad] Complete signup.html
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 02_git_branch/signup.html

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git log --oneline
2d928ad (HEAD -> feature/signup) Complete signup.html
7b7e648 (origin/master, master) completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/signup 
Switched to branch 'feature/signup'

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   02_git_branch/merge-test.txt


student@M1305 MINGW64 ~/TIL (master)
$ git commint -m "updated merge-test.txt file"
git: 'commint' is not a git command. See 'git --help'.

The most similar command is
        commit

student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "updated merge-test.txt file"
[master 4716c64] updated merge-test.txt file
 1 file changed, 1 insertion(+)

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
4716c64 (HEAD -> master) updated merge-test.txt file
7b7e648 (origin/master) completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/signup
Switched to branch 'feature/signup'

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git log --oneline
2d928ad (HEAD -> feature/signup) Complete signup.html
7b7e648 (origin/master) completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (feature/signup)
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git merge feature/signup 
Merge made by the 'recursive' strategy.
 02_git_branch/signup.html | 0
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 02_git_branch/signup.html   

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
adb7154 (HEAD -> master) Merge branch 'feature/signup'
4716c64 updated merge-test.txt file
2d928ad (feature/signup) Complete signup.html
7b7e648 (origin/master) completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline --graph
*   adb7154 (HEAD -> master) Merge branch 'feature/signup'
|\
| * 2d928ad (feature/signup) Complete signup.html
* | 4716c64 updated merge-test.txt file
|/
*   7b7e648 (origin/master) completed merge
|\  
| * 67d2a3f Complete test.html
* |   ace5fe1 Merge branch 'feature/test'
|\ \  
| |/
| * 97970bd added merge-test.txt
* | 41f9e38 commit
|/
* 35557ad updated .gitignore
* ede9fb5 added reset.txt and omit_file.txt files
* c8a4402 Added reset.txt and reset2.txt
* 7044b09 added .gitignore file
* 933b778 added Git.md file
* 65579e4 second commit
* 02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git branch
  feature/signup
* master

student@M1305 MINGW64 ~/TIL (master)
$ git branch --d feature/signup 
Deleted branch feature/signup (was 2d928ad).

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
adb7154 (HEAD -> master) Merge branch 'feature/signup'
4716c64 updated merge-test.txt file
2d928ad Complete signup.html
7b7e648 (origin/master) completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline --graph
*   adb7154 (HEAD -> master) Merge branch 'feature/signup'
|\
| * 2d928ad Complete signup.html
* | 4716c64 updated merge-test.txt file
|/
*   7b7e648 (origin/master) completed merge
|\
| * 67d2a3f Complete test.html
* |   ace5fe1 Merge branch 'feature/test'
|\ \
| |/
| * 97970bd added merge-test.txt
* | 41f9e38 commit
|/
* 35557ad updated .gitignore
* ede9fb5 added reset.txt and omit_file.txt files
* c8a4402 Added reset.txt and reset2.txt
* 7044b09 added .gitignore file
* 933b778 added Git.md file
* 65579e4 second commit
* 02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$

```



```bash

student@M1305 MINGW64 ~/TIL (master)
$ git branch
* master

student@M1305 MINGW64 ~/TIL (master)
$ git push origin master
Enumerating objects: 13, done.
Counting objects: 100% (13/13), done.
Delta compression using up to 8 threads
Compressing objects: 100% (9/9), done.
Writing objects: 100% (10/10), 924 bytes | 924.00 KiB/s, done.
Total 10 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 1 local object.
To https://github.com/JHM9191/TIL.git
   7b7e648..adb7154  master -> master

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
adb7154 (HEAD -> master, origin/master) Merge branch 'feature/signup'
4716c64 updated merge-test.txt file
2d928ad Complete signup.html
7b7e648 completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git checkout -b feature/board
Switched to a new branch 'feature/board'

student@M1305 MINGW64 ~/TIL (feature/board)
$ git status
On branch feature/board
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   00_git_intro/todaygit.md
        modified:   02_git_branch/merge-test.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@M1305 MINGW64 ~/TIL (feature/board)
$ git add .

student@M1305 MINGW64 ~/TIL (feature/board)
$ git commit -m "updated merge-test.txt file"
[feature/board 100298b] updated merge-test.txt file
 2 files changed, 1051 insertions(+), 2 deletions(-)

student@M1305 MINGW64 ~/TIL (feature/board)
$ git log --oneline
100298b (HEAD -> feature/board) updated merge-test.txt file
adb7154 (origin/master, master) Merge branch 'feature/signup'
4716c64 updated merge-test.txt file
2d928ad Complete signup.html
7b7e648 completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (feature/board)
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
adb7154 (HEAD -> master, origin/master) Merge branch 'feature/signup'
4716c64 updated merge-test.txt file
2d928ad Complete signup.html
7b7e648 completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   02_git_branch/merge-test.txt

no changes added to commit (use "git add" and/or "git commit -a")

student@M1305 MINGW64 ~/TIL (master)
$ git add .

student@M1305 MINGW64 ~/TIL (master)
$ git commit -m "updated merge-test.txt file python -> java"
[master 49d6cd3] updated merge-test.txt file python -> java
 1 file changed, 1 insertion(+), 1 deletion(-)

student@M1305 MINGW64 ~/TIL (master)
$ git log --oneline
49d6cd3 (HEAD -> master) updated merge-test.txt file python -> java
adb7154 (origin/master) Merge branch 'feature/signup'
4716c64 updated merge-test.txt file
2d928ad Complete signup.html
7b7e648 completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (master)
$ git checkout feature/board 
Switched to branch 'feature/board'

student@M1305 MINGW64 ~/TIL (feature/board)
$ git log --oneline
100298b (HEAD -> feature/board) updated merge-test.txt file
adb7154 (origin/master) Merge branch 'feature/signup'
4716c64 updated merge-test.txt file
2d928ad Complete signup.html
7b7e648 completed merge
67d2a3f Complete test.html
ace5fe1 Merge branch 'feature/test'
41f9e38 commit
97970bd added merge-test.txt
35557ad updated .gitignore
ede9fb5 added reset.txt and omit_file.txt files
c8a4402 Added reset.txt and reset2.txt
7044b09 added .gitignore file
933b778 added Git.md file
65579e4 second commit
02946c0 first commit

student@M1305 MINGW64 ~/TIL (feature/board)
$ git checkout master
Switched to branch 'master'

student@M1305 MINGW64 ~/TIL (master)
$ git merge feature/board
Auto-merging 02_git_branch/merge-test.txt
CONFLICT (content): Merge conflict in 02_git_branch/merge-test.txt
Automatic merge failed; fix conflicts and then commit the result.

student@M1305 MINGW64 ~/TIL (master|MERGING)
$

```

