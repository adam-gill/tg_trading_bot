### Telegram Bot 
### Design Specifications
> Team Kyle Jan 2024

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
