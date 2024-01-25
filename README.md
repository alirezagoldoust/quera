# Welcome to QueraQuestion documentation!
This project is back-end implementation of [Quera.org](https://quera.org/) question asking software.<br>
It was written with python-django and REST framewrok and also JWT for Authentication.<br>
## How to use:
Befor you start using the project you need to create your own .env file that the contents should be like [sample_env](https://github.com/alirezagoldoust/quera/blob/492f4972471234f2245d2a7465f39b5d9a012857/sample_env).<br>
Also the database is postgres.<br><br>
In order to use the project better, befor use you can run [init.py](https://github.com/alirezagoldoust/quera/blob/9dd166e2ed2258254c589347a0ef0631e5f612aa/init.py) file to add a sample data to your database.
Also you can add [postman_collection](https://github.com/alirezagoldoust/quera/blob/08d1dfe36a0f667e67dd4e17d966f5ec99332021/Quera.postman_collection.json) requests to your postman in order to have sample requests.<br><br>
The program can be used with authentication, so you should create account befor use it.
### Creating account
you should give a username, password in request body, then it returns access token and refresh token.
```
(post):api/signup/

body:
{
  username='username',
  password='password'
}
```
### Login
You can take your token if lost or expired with entering username and password in request body.
```
(post):api/login/

body:
{
  username='username',
  password='password'
}
```
### Refresh Token
```
(post):api/token/refresh
```
### Add question
This request requires Athentication, and you should specify the source of question you wanna ask(teacher or qgpt), the problem name and the question_text.
```
(post):api/question/add/
body:
{
    "from": "teacher",
    "problem" : "problem_name",
    "question_text": "question_text"
}
```
The view uses multipartparser, so you should use form-data format to send your body request.<br>
image, appendix are optional
### List my questions
This request requires Athentication.
```
(get):api/question/list/
```
### Update question
This request requires Athentication, and you should specify the source of question you asked(teacher or qgpt) and the question_id in query_prams and you can change the question_text, image, appendix fields in your request body.
(question_id can be found in question list request)
```
(patch):api/question/update/?source=teacher&id=30
body:
{
    "question_text": "new_question_text"
}
```
It's recommended use form-data format to send your body request due to working with files.<br>
image, appendix are optional<be>
### Delete question
This request requires Athentication, and you should specify the source of question you asked(teacher or qgpt) and the question_id in query_prams.
(question_id can be found in question list request)
```
(delete):api/question/delete/?source=teacher&id=30
```
## More detail about program structure
For generating title of questions (and answer for gpt asked questions) I used OpenAI API.<br>
To use that service you should put your OPENAI_API_KEY in .env file.<br>
If you are running the project in Iran it's likely to face ConnectionError using this service :)<br>
But you can test the service in google colab notebook.<br>
