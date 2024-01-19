# Telegram Bot
## Design Specifications
### Team Kyle Jan 2024

## Telegram Bot UI:

## Translator:
The Translator is the front-most facing backend module of the Telegram bot. When the server receives a message from the user, the Translator translates the message into DuneSQL and encoded logic and stores it in the Database. Uses a serialized logic representation for translation of encoded logic.

## Database:
This project uses a relational database. It will be organized into three tables: **users**, **events**, and **queries**.


## Data receiver:
