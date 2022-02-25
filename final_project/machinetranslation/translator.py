"""
This file contains every method for translating
from english to french and viceversa using IBM Watson api
"""
# thrid party modules

#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']

url = os.environ['url']

try:
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3( version='2018-05-01',
    authenticator=authenticator)
    INSTANCE = 'https://api.eu-gb.language-translator.watson.cloud.ibm.com'
    language_translator.set_service_url(INSTANCE)
    print("Instance created!")

except Exception as e: # pylint: disable=W0703
    print("Error. Reason: "+e)

def english_to_french(english_text):
    """
    args: english text
    returns: french text
    """
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    #print(json.dumps(translation, indent=2, ensure_ascii=False))
    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """
    args: french text
    returns: english text
    """
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text= translation['translations'][0]['translation']
    return english_text
