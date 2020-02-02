# LoginSystem
A simple yet secure login and register system using;
- Flask
- passlib
- PyJWT
- SQLAlchemy

Feel free to use it as a base template to speed up work on any other projects.

## Setup
To run simply type `py app.py`. The webpage will run on `localhost:5000` by default.

If you want to reset the database, delete main.db from routes directory then open an IDLE and type:
```
import db from routes.auth
db.create_all()
quit()
```

## Register screen: 
![Register screen](https://i.imgur.com/2RST4s2.png)

## Login screen: 
![Login screen](https://i.imgur.com/CHpV7u7.png)

## Main screen: 
![Main screen](https://i.imgur.com/mvQbZTU.png)
