# Quiz Project Instruction

## Project Stack

|  Name       | Version  |
|-------------|----------|
|  Python     | 3.11   	 |
|  Sqlalchemy | 2.0.10 |


## Development Environment Configuration

## Clone Project

The first things to do is to clone the repository.

### Python Env Setup

create a virtual environment to install dependencies inside it and active it.

#### poetry package

Install poetry package

```sh
pip install poetry --upgrade
```

Create Virtual Environment and install dependencies command is:

```sh
poetry install 
```

Activate virtual environment
_____________________________________________________

The MVP (Model-View-Presenter) architecture is used in this program, with an SQLite database and ORM (Object-Relational Mapping) using sqlalchemy for simplicity. To access the program, an account is required. You have the option to register as a regular user or as a superuser by using a security code. For convenience, a superuser account with the following username and password has already been created in the database.

***username:*** __admin__
***password:*** __12345678a__

You can also create a new admin user for yourself by entering the security code provided:

***Security Code:*** __VAIdrFPnUvs__

Upon creating a user, 5 questions out of 10 in the database will be randomly selected, each with a value of 20 points. After answering the questions, the user's score will be calculated and displayed. If the user is a superuser, they can access the admin panel, where they can insert and delete questions from the database.



