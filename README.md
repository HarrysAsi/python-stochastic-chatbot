***_Stochastic AI chatbot_***

This is a simple AI chatbot made with python tensorflow.
Also, it contains a simple django UI implementation in order to help you create your own dataset.

**_Chatbot Installation_**

Go to the bot's root directory
```
cd bot
```

Python Environment
```
Create your python virtual env
```

Install dependencies
```
pip install poetry && poetry install
```

Command to train the bot:
```
python -m training
```
Command to run the bot:
```
python -m chatbot
```
Command to parse the extracted data from the django app:
```
python -m parser
```

**_Web App Installation_**

Go to the web's app root directory
```
cd web
```


Python Environment
```
Create your python virtual env
```

Install dependencies
```
pip install poetry && poetry install
```

Start the server
```
python manage.py runserver
```

Open your browser and navigate to:
```
http://localhost:8000
```

*_Note_*
You can start adding your own questions / answers which you would like to train the bot with!

*_Note_*
Once you are done, download the data, use the existing parser to parse all its content and start using your bot!

**_Author_**

* **Asimakopoulos Charalampos** - *Initial work* - [HarrysAsi](https://github.com/HarrysAsi)