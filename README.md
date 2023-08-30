# Website_Project-Frontend-Backend-with-Database-

This README provides a comprehensive guide to setting up and running your website project, including the installation of PostgreSQL, pgadmin4, FastAPI, and SQLAlchemy, as well as creating both the backend and frontend components of the website.

## Table of Contents

- [PostgreSQL Database Installation (Ubuntu)](#postgresql-database-installation-ubuntu)
- [pgadmin4 Installation (Ubuntu)](#pgadmin4-installation-ubuntu)
- [FastAPI Installation (Ubuntu)](#fastapi-installation-ubuntu)
- [SQLAlchemy Installation (Ubuntu)](#sqlalchemy-installation-ubuntu)
- [Creating the Website](#creating-the-website)
  - [Backend](#backend)
  - [Frontend](#frontend)

## PostgreSQL Database Installation (Ubuntu)

1.Create the file repository configuration:
    
    ```bash
    #sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    ```
2.Import the repository signing key:
    
    ```bash
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    ```
3.Update the package lists:
    
    ```bash
    sudo apt-get update
    ```
4.Install the latest version of PostgreSQL:
    
    ```bash
    sudo apt-get -y install postgresql
    ```
5.Start, stop, and check the status of the server:
    
    ```bash
    sudo systemctl start postgresql
    ```
    ```bash
    sudo systemctl stop postgresql
    ```
    ```bash
    sudo systemctl status postgresql
    ```
6.Access the PostgreSQL command-line interface:
    
    ```bash
    sudo -u postgres psql
    ```
7.Create a new PostgreSQL user:
    
    ```bash
    createuser --interactive --username=yourusername
    ```
    - To see the users: \du
    - To see databases: \l
    - To create a database: create database database_name
    - To select a database to use: \c database_name
    - To exit: \q

## pgadmin4 Installation (Ubuntu)

1.Install the public key for the repository:

  ```bash
  curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg
  ```
2.Create the repository configuration file:

  ```bash
  sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'
  ```
3.Install pgadmin4:

- For both desktop and web modes:
  ```bash
  sudo apt install pgadmin4
  ```
- For desktop mode only:
  ```bash
  sudo apt install pgadmin4-desktop
  ```
- For web mode only:
  ```bash
   sudo apt install pgadmin4-web
  ```
4.Configure the webserver (if using pgadmin4-web):
  ```bash
  sudo /usr/pgadmin4/bin/setup-web.sh
  ```
5.Open pgadmin4 and add a new server with hostname as "localhost".

## FastAPI Installation (Ubuntu)

1.Open the terminal and install FastAPI:

  ```bash
  pip install fastapi
  ```
2.Install the server on which FastAPI will run:

  ```bash
  pip install "uvicorn[standard]"
  ```

## SQLAlchemy Installation (Ubuntu)

1.Install SQLAlchemy:
  ```bash
  pip install sqlalchemy
  ```
## Creating the Website

# Backend:

Follow these steps to create CRUD APIs for database operations:

Set up the file structure as described in the project directory.

Create SQLAlchemy parts in application/database.py.

Define database models in application/models.py.

Create Pydantic models in application/schemas.py.

Implement CRUD utilities in application/crud.py.

Create the main FastAPI app in application/main.py.

Run the app with Uvicorn:

lua
Copy code
uvicorn application.main:app --reload
Access the interactive environment at http://127.0.0.1:8000/docs.

Frontend:
Follow these steps to create webpages that interact with users and send data to APIs:

Create HTML, CSS, and JavaScript files for the frontend components.

Handle CORS (Cross-Origin Resource Sharing) appropriately in the backend (refer to application/main.py).

Run a local server to host your frontend:

yaml
Copy code
python3 -m http.server 8085
Access the website in your browser at http://127.0.0.1:8085/.

The entered data will be stored in the database (use pgadmin4 to view the data).

Feel free to adapt these instructions to your specific project structure and requirements. Good luck with your website project!
