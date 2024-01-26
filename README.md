# Welcome to QueraQuestion documentation!
This project is back-end implementation of [Quera.org](https://quera.org/) question asking software.<br>
It was written with python-django and REST framewrok.<br>
## How to use:
Befor you start using the project you need to:<br>
1.create virtual environment and install [requirements.txt](https://github.com/alirezagoldoust/quera/blob/cff1aa4aadd1f406cf30d3dcd466e19dd335cbe1/requirements.txt)<br>
2.create your own .env file that the contents should be like [sample_env](https://github.com/alirezagoldoust/quera/blob/492f4972471234f2245d2a7465f39b5d9a012857/sample_env).<br>
Also the database is PostgreSQL.<br><br>
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
The Q-GPT asked questions and teacher asked questions are saved in two seprated table models in api app. It's good to mention that the used database is PostgreSQL.<br><br>
The media uploaded from users will be saved in a folder called 'uploaded_files'.<br><br>
Authentication of the program is perform by RESTframework_simpleJWT and the provided access_tokens are valid for 30 Minutes.<br><br>
For generating title of questions (and answer for gpt asked questions) I used OpenAI API. To use that service you should put your OPENAI_API_KEY in your .env file.<br>
And if you are running the project in Iran it's likely to face ConnectionError while using this service :) so if you use [shekan](https://shecan.ir/) DNS it will be solved.<br><br>
Hope you enjoy it ;)

