# Mova Pizza (Flask & mysql)

```git clone``` the repository and ```cd``` into the app directory.

#### Run the app
- create a mysql database and update the following line in ```__init__.py``` like ```app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://YourUsername:Yourpassword@localhost/dbName'```
- create the enviroment with ```virtualenv <yourEnviromentName>```  
- Install all the requirements in your environment.

`pip install -r requirements.txt`

After that, run the app using the command.

`python run.py`

Access the homepage on `http://localhost:5000`