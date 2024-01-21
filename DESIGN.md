<h1 align="center"> Telegram Bot </h1> <br>
<p align="center">
  <a href="https://gitpoint.co/">
    <img alt="GitPoint" title="GitPoint" src="http://i.imgur.com/VShxJHs.png" width="450">
  </a>
</p>

<p align="center">
  GitHub in your pocket. Built with React Native.
</p>

<p align="center">
  <a href="https://itunes.apple.com/us/app/gitpoint/id1251245162?mt=8">
    <img alt="Download on the App Store" title="App Store" src="http://i.imgur.com/0n2zqHD.png" width="140">
  </a>

  <a href="https://play.google.com/store/apps/details?id=com.gitpoint">
    <img alt="Get it on Google Play" title="Google Play" src="http://i.imgur.com/mtGRPuM.png" width="140">
  </a>
</p>
## Telegram Bot UI:

## Backend:
The backend includes three basic modules: **Translator**, **Database**, and **Data Retriever**.
<br />
### Translator:
The Translator is the front-most facing backend module of the Telegram bot. When the server receives a message from the user, the Translator translates the message into DuneSQL and encoded logic and stores it in the Database.
<br />
Runs **Data Retriever**
## Database:
This project uses a relational database. It will be organized into three tables: **users**, **events**, and **queries**.

A rough outline of the database structure is shown below:
![Screenshot 2024-01-19 at 3 10 55 PM](https://github.com/adam-gill/tg_trading_bot/assets/81604772/1e94b320-315a-4233-bd5f-c2363181a87e)



## Data Retriever:
