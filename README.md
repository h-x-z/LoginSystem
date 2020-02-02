# LoginSystem
Simple login and register system using;
- Flask
- passlib
- PyJWT
- SQLAlchemy

## Setup
To run simply type `py app.py`, if you want to reset the db, delete the main.db from routes then type open an IDLE and type:
```
import db from routes.auth
db.create_all()
```
The webpage will run on `localhost:5000` by default.

## Register screen: 
![Register screen](https://i.imgur.com/2RST4s2.png)

## Login screen: 
![Login screen](https://i.imgur.com/CHpV7u7.png)

## Main screen: 
![Main screen](https://i.imgur.com/mvQbZTU.png)
