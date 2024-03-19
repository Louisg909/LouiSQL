
# Todo
- Required validation doesn't seem to do anything when making tables - need to check why this is
    - I worked out why this is - if something isn't given as an argument, it is never put to be validated meaning it isn't checked whether it is there or not... bit silly lol. Not going to look into it now but I presume the issue can be solved by maybe doing something with kwargs or something. Not sure, just look into it next time.


# Ideas
- Might be a cool idea for querying to be written as a single query function, using SQL input which will be processed and used? Idk how viable it would be but it would make it a lot easier to learn and straight forward than learning a new language like you have to do with Flask-SQLAlchemy
