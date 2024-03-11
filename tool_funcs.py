import glob
import json
import os
from configparser import ConfigParser

import dearpygui.dearpygui as dpg
import pyautogui as pt
import pytesseract
import requests
from PIL import Image

config = ConfigParser()
config.read('app_settings.ini')
screenshot_dir = config['app_settings']['screenshot_filepath']
api_key = config['app_settings']['api_key']
image_mod_time = 0
latest_image = None
prompt_add = "Read the following multiple-choice question and identify the correct answer(s). Output the response using periods only. No additional text should be included in the response."

#get latest image from screenshot dir
#parse text from image
#make gpt prompt using text
#receive answer back from gpt
#print out answer
#wait 3sec for next image
#rerun until program is closed

def start_btn_callback():
    prompt = parse_image()
    return gpt_ask(prompt, api_key)

def move_btn_callback():
    mousePos = pt.position()
    dpg.set_viewport_pos(mousePos)
def parse_image():
    img = get_latest_image(screenshot_dir, image_mod_time)
    return get_text_from_image(img)
def get_latest_image(dir, mod_time):
    for image in glob.glob(dir):
        latest_image_time = os.path.getmtime(image)
        if latest_image_time > mod_time:
            mod_time = latest_image_time
            latest_image = image
    return latest_image

def get_text_from_image(img):
    img_text = pytesseract.image_to_string(Image.open(img))
    return img_text

def gpt_ask(question, key):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + key,
    }

    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': prompt_add + question,
            },
        ],
        'temperature': 0.1,
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
    response_string = json.dumps(response.json())
    response_dict = json.loads(response_string)
    print(response_dict['choices'][0]['message']['content'])
    return response_dict['choices'][0]['message']['content']
