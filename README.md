## Lunch Ticket Application
* Lunch ticket control application with qrCode generation.

## Requirements
* [Python3](https://www.python.org/)
* [Pip](https://pypi.python.org/pypi/pip)
* [Virtualenv](https://virtualenv.pypa.io/en/stable/)
* [NodeJS](https://nodejs.org/)

## Installation / Usage
* #### Install Python & Pip on windows
    * https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation

* Ensure you have python3 globally installed in your computer.
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
    $ pip install virtualenv
    ```

* #### Install the requirements
    ```
    (venv)$ pip install -r requirements.txt
    ```

* #### Migrations
    Migrations commands
    ```
    (venv)$ python manage.py db init (creates a new migrations folder)
    ```

    ```
    (venv)$ python manage.py db migrate --message "your message" (creates a new migration file)
    ```

    Migrate your migrations to persist on the DB
    ```
    (venv)$ python manage.py db upgrade (apply the migrations to the database)
    ```


* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ python run.py
    ```
    You can now access the app on your local browser by using


## Documentation
* #### Backend
    * [Flask](http://flask.pocoo.org/)
    * [Flask Restful and Swagger](https://github.com/swege/flask-restful-swagger-2.0)
    * [Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.3/)
    * [Flask-Alembic](https://flask-alembic.readthedocs.io/en/stable/)
    * [Flask-Swagger-UI](https://github.com/sveint/flask-swagger-ui)
    * [Flask-JWT](https://pythonhosted.org/Flask-JWT/)
    * [SQLAlchemy](https://www.sqlalchemy.org/)
    * [Alembic](https://pypi.python.org/pypi/alembic)
    * [PyQRCode](https://pypi.python.org/pypi/PyQRCode)
* #### Frontend
    * [ReactJS](https://reactjs.org/)
    * [NodeJS](https://nodejs.org/)
    * [WebPack](https://webpack.js.org/)
    * [TypeScript](https://www.typescriptlang.org/)
    * [CSS Module](https://github.com/css-modules/css-modules)
    * [Jest](https://facebook.github.io/jest/)
    * [Enzyme](http://airbnb.io/enzyme/)

## Developer Tools
* React Developer Tools
    * https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en
* Redux Developer Tools
    * https://github.com/zalmoxisus/redux-devtools-extension

## For windows users using pycharm
* If you are on the windows environment and want to use cmder with pycharm you can do
* Create a environment variable
    ```
    CMDER_ROOT = C:\cmder (for example)
    ```
* On pycharm edit the terminal shell path like this
    ```
    "cmd.exe" /k ""%CMDER_ROOT%\vendor\init.bat"" is important have all the quotes
    ```
