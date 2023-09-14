import requests
from Config import PROXY
import json

class QuestionService:
    def get_questions(**kwargs)-> dict:
        return requests.get(PROXY + 'get_questions', params=kwargs).json()

    def get_question(id)-> dict:
        return requests.get(PROXY + 'get_question/'+str(id)).json()

    def get_quiz_name()->dict:
        return requests.get(PROXY +'get_quiz_name/1' ).json()
    

