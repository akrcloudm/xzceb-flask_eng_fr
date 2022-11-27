"""Instantiates language translator instance and defines translation functions"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('YGYNy-KbSCvuOye-QdVrZ-CelgAoFC9ntMZhBYRRWH0m')

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/6fbeed73-d011-4942-86c5-fd82f034f388')
def english_to_french(text1):
    """This function translates English to French"""
    frenchtranslation=language_translator.translate(text=text1,model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(text1):
    """This function translates French to English"""
    englishtranslation=language_translator.translate(text=text1,model_id='fr-en').get_result()
    return englishtranslation.get("translations")[0].get("translation")
