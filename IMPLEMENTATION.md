# Telegram Bot
## Implementation Details
### Team Kyle Jan 2024

## Project Architecture Diagram:
![Proj_arch_draft2](https://github.com/adam-gill/tg_trading_bot/assets/81604772/8b6f2fb3-c168-4659-b834-e8acb87e110b)


## Telegram Bot UI:


## Translator:
The Translator is the front-most facing backend module of the Telegram bot. When the server receives a message from the user, the Translator translates the message into DuneSQL and encoded logic and stores it in the Database. Uses a serialized logic representation for translation and storage of encoded logic.

## Database:
This project uses a relational database. It will be organized into three tables: **users**, **events**, and **queries**.

A rough outline of the database structure is shown below:
![Screenshot 2024-01-19 at 3 10 55 PM](https://github.com/adam-gill/tg_trading_bot/assets/81604772/1e94b320-315a-4233-bd5f-c2363181a87e)



## Data receiver:
