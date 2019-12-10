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



**HEAD**

- git에 있는 특수한 포인터
- 가장 최신의 경로?



![image-20191210160649993](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210160649993.png)

![image-20191210160658080](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210160658080.png)





















