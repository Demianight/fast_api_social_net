# Social network

Simple social network API.

## Why

I made it to practice FastAPI and other techs.

## How

It's built on:

- FastAPI
- SQLModel
- bcrypt
- SQLite3

## What's interesting

All points in the list was made by me for the first time:

- Password hashing
- Token generation and validation
- Email confirmation and backrgound tasks
- Triple Depends dependency (first expirience)
- Custom authorization in FastAPI
- Custom crud
- First expirience with routers

## TODO:

- Make posts require auth and actually connect User to Post model.
- Connect redis-cache
- Improve crud classes
- Connect Celery???
- Make Docker
- Improve model's validation
