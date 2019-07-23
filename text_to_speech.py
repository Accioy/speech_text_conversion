#coding=utf-8
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '...'
API_KEY = '...'
SECRET_KEY = '...'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


text='What the fuck.'
result  = client.synthesis(text, 'zh', 1, {
    'vol': 5,
    'per':1
})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)

from playsound import playsound
playsound('audio.mp3')
