## Git에 대하여



### 1. Git 초기 설정

```bash
# 현재 PC에 어떤 계정으로 연결이 되어 있는지 확인한다.
$ git config --global --list

# 내 아이디와 내 이메일이 아니면 이름을 설정해준다.
$ git config --global user.name "JHM9191"

# 이메일도 설정해준다.
$ git config --global user.email "hm.jo.9191@gmail.com"

```



### 2. 파일 생성

```bash
# 현재 최상위 폴더가 무엇인지 확인.
$ ls

# Git.md라는 파일을 00_git_intro폴더 아래에 생성한다.
$ touch 00_git_intro/Git.md

# git 상태 확인.
$ git status

# 현재 폴더(Working Directory)에 있는 untracking하고 있는 모든 폴더 및 파일을 staging area에 올린다.
$ git add .

# 
$ git status

# commit을 하여 GitHub Repository에 올린다.
$ git commit -m "added Git.md file"


```





### 3. git add, commit, push

```bash
$ git add [파일/폴더명]

$ git commit -m "커밋 메세지"

$ git push origin master
```



### 4. log를 찍는 방법









### 5. github repository의 원격저장소(remote)와 연동하는 방법

```bash
# origin이라고 하는 이름으로 remote 생성하기.
$ git remote add origin [github/bucket/gitbal remote URL]
# 주소는 Clone or download 라고 하는 버튼을 클릭하면 보이는 주소임. 

# 이 repository가 어떤 remote와 연결되어 있는지 확인할 수 있음.
$ git remote -v

#
$ git remote rename 현재이름 바꿀이름 
$ git remote rename origin jhm

# remote 삭제하기
$ git remote rm jhm
```





### 6. 원격저장소로 보내고 원격저장소에서 받아오기

```bash
#local에서 저장한걸 원격으로 보내는 명령어
$ git push orgin master

# local로 가져오는 명령어
$ git pull origin master

# 최초 1회 다운로드할 때 사용하는 명령어
$ git clone origin master
# 계정 비번 입력하라고 함. 


# 대표적인 실수
# 집에 왔는 데 깜박하고 pull을 안한 경우. 
# pull을 해야하 동기화가 되는데 pull안한 상태에서 
# 작업을 하고 commit을 했을 때 에러가 발생함. 

```







깃 이닛은 하나의 디렉토리에 여러개가 있을 수 없음.



## A

```bash
cd ..

mkdir endgame

cd endgame

touch endgame.txt README.md

# Github collaborating log

endgame.txt

자장면


동욱씨는 "멀티캠퍼스" 라고 쓰심. 

$ git status
$ git add .
$ git commit -m "first turn"


새로운 repository 만들기. 
repository 이름은 endgame.


$ git remote add origin https:~~
$ git remote -v
$ git push origin master



```



## B

```bash
git bash에서..

$ git clone https://github.com/hyunro19/endgame.git
$ cd endgame/

endgame 폴더로 들어와서 우클릭한다음에 vscode로 열기를 해줌. 

멀티캠퍼스를 이어서 내가 스택오버플로우를 써줌. 

그런 다음 vs code 터미널에서 




git add .
git commit -m "second turn"
git remote push origin master

하면 에러 뜸. 

A가 B에게 권한을 안 줬기 때문.

A가 B에게 Github에서 setting들어가서 해당 repository에 대한 링크를 보냄.
(초대권을 보내는 것임.)

이메일로 초대권 받음. 

이메일로 초대 수락함. 


그리고 나서 git push origin master를 해주니까 

정상적으로 push가 됨. 


그리고 나서 github에서 repository에 들어가서 새로고침을 하니까 
내가 수정한 second turn이 올라와 있음. 


```





### A

``` bash
# remote 에 있는 내용이 local로 내려옴.
$ git pull origin master

$ git add .
$ git commit -m "third turn"

$ git push origin master



```



### B

```bash
github에서 새로고침을 해보니 
동욱씨가 "우사단로"라고 추가 하심. 

#충돌 내실거라고 함. 

#원래라면 git pull origin master 를 해줘야하지만. 
# pull 하지 않은 상태에서 내가 3번 라인에 우사인볼트라고 써보기.

$ git add .
$ git commit -m "fourth turn"

student@M1305 MINGW64 ~/endgame (master)
$ git add .

student@M1305 MINGW64 ~/endgame (master)
$ git commit -m "fourth turn"
[master bb044d9] fourth turn
 1 file changed, 2 insertions(+), 1 deletion(-)

student@M1305 MINGW64 ~/endgame (master)
$ git push origin master
To https://github.com/hyunro19/endgame.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/hyunro19/endgame.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
이렇게 에러가 뜸. 


git pull... 풀 먼저하라고 힌트알려줌.

$ git pull origin master

student@M1305 MINGW64 ~/endgame (master)
$ git pull origin master
From https://github.com/hyunro19/endgame
 * branch            master     -> FETCH_HEAD
Auto-merging endgame.txt
CONFLICT (content): Merge conflict in endgame.txt
Automatic merge failed; fix conflicts and then commit the result.


incoming line 
current line 이렇게 뜸.






```



![pull을 먼저 안해줘서 나오는 충돌상황에 pull 해주면 이렇게 뜸.](C:\Users\student\AppData\Roaming\Typora\typora-user-images\image-20191210134300075.png)

> pull을 먼저 안해줘서 나오는 충돌상황에 pull 해주면 이렇게 뜸.



#### 선택 사항

- Accept Current Change
- Accept Incoming Change
- Accept Both Changes
- Compare Changes

