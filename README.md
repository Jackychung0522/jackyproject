#乒乓球不專業教練

#構想
本身有學過乒乓球，希望藉由這次的作業可以把一些打乒乓球會遇到的問題或是想要增進自己的哪一部分寫成一個聊天機器人，利用影片因材施教的方式讓不管已經沒有基礎，或是打過一段時間的人，都能夠在球技上更上一層樓!

## 環境
- ubuntu 18.04
- python 3.6.9

#使用說明
-輸入任意文字進入到user的state 他會問你想不想要進入桌球的世界 打想要
-接著會有**初學者** 、**中級** 和**高級** 三個等級讓你選擇 ，使用者選擇自己對應的程度。
-選進去之後，各自都有今天想要加強的部分，分為 **發球** 、**接發球**、和**必殺技**
-其中接發球又分為三種球路，問說你遇到的是哪一種球 **上旋** **下旋**還是**側旋球**
-而點進去之後各自會有教學的影片，其中必殺技都是自己拍攝的，而其餘的皆是網路上的教學影片

帳號:電子郵件gmail
密碼是 5p1158jab-

# Jacky final project 乒乓球不專業教練

[![Maintainability](https://api.codeclimate.com/v1/badges/dc7fa47fcd809b99d087/maintainability)](https://codeclimate.com/github/NCKU-CCS/TOC-Project-2020/maintainability)

[![Known Vulnerabilities](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020/badge.svg)](https://snyk.io/test/github/NCKU-CCS/TOC-Project-2020)


## 構想
本身有學過乒乓球，希望藉由這次的作業可以把一些打乒乓球會遇到的問題或是想要增進自己的哪一部分寫成一個聊天機器人，利用影片因材施教的方式讓不管已經沒有基礎，或是打過一段時間的人，都能夠在球技上更上一層樓!

## 環境
- ubuntu 18.04
- python 3.6.9
## 使用說明

- 輸入任意文字進入到user的state，他會問你想不想要進入桌球的世界，案想要的話進入，案離開的話離開
- 接著會有**初學者** 、**中級** 和**高級** 三個等級讓你選擇 ，使用者選擇自己對應的程度。
- 選進去之後，各自都有今天想要加強的部分，分為 **發球** 、**接發球**、和**必殺技**
- 其中接發球又分為三種球路，問說你遇到的是哪一種球 **上旋** **下旋**還是**側旋球**
- 而點進去之後各自會有教學的影片，其中必殺技都是自己拍攝的，而其餘的皆是網路上的教學影片
## 使用教學
1. install `pipenv`
```shell
pip3 install pipenv
```
2. install 所需套件
```shell
pipenv install --three
// 若遇到pygraphviz安裝失敗，則嘗試下面這行
sudo apt-get install graphviz graphviz-dev
```
3. 從`.env.sample`產生出一個`.env`，並填入以下兩個資訊

- Line
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN
4. install `ngrok`

```shell
sudo snap install ngrok
```
5. run `ngrok` to deploy Line Chat Bot locally
```shell
ngrok http 8000
```
6. execute app.py
```shell
python3 app.py
```

## 使用說明
- 基本操作
    - 所有用到英文的指令大小寫皆可
    - 隨時輸入任何字若沒觸發到都會有提示
    - 含有button或是以文字輸入切換到下一個state
## Finite State Machine
![image](https://github.com/Jackychung0522/jackyproject/blob/master/my_state_diagram.png)
### state說明
- user:初始化步驟，問說想要進入桌球世界嗎，選擇想要繼續，選擇離開則跳到state1
- state1:存放離開的state，在後面的步驟如果有離開案件按下後，則會跳到此state再自動跳回user state
- age:等級分為初級，中級，和高手
- medium:中級
- beginner:初級
- highlevel:高級
- serve結尾:各級的發球
- served結尾:各級的接發球
- killer結尾:各級的必殺技
- finish結尾:各級的結束，結束後可以選擇離開或是觀看另外幾種技術的影片。
- servedtop結尾:各級的上旋接發球
- servedside結尾:各級的側旋接發球
- servedunder結尾:各級的下旋接發球
## 使用示範
![](https://img.onl/rek8l7)
![](https://img.onl/swa8EN)
![](https://img.onl/FdLpry)
![](https://img.onl/lkiM9x)

Setting to deploy webhooks on Heroku.

### Heroku CLI installation

* [macOS, Windows](https://devcenter.heroku.com/articles/heroku-cli)

or you can use Homebrew (MAC)
```sh
brew tap heroku/brew && brew install heroku
```

or you can use Snap (Ubuntu 16+)
```sh
sudo snap install --classic heroku
```

### Connect to Heroku

1. Register Heroku: https://signup.heroku.com

2. Create Heroku project from website

3. CLI Login

	`heroku login`

### Upload project to Heroku

1. Add local project to Heroku project

	heroku git:remote -a {HEROKU_APP_NAME}

2. Upload project

	```
	git add .
	git commit -m "Add code"
	git push -f heroku master
	```

3. Set Environment - Line Messaging API Secret Keys

	```
	heroku config:set LINE_CHANNEL_SECRET=your_line_channel_secret
	heroku config:set LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
	```

4. Your Project is now running on Heroku!

	url: `https://jackychatbox.herokuapp.com/webhook`

	debug command: `heroku logs --tail --app {jackychatbox}`

5. If fail with `pygraphviz` install errors

	run commands below can solve the problems
	```
	heroku buildpacks:set heroku/python
	heroku buildpacks:add --index 1 heroku-community/apt
	```

	refference: https://hackmd.io/@ccw/B1Xw7E8kN?type=view#Q2-如何在-Heroku-使用-pygraphviz
