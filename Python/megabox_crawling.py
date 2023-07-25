import requests
from bs4 import BeautifulSoup
import json, sys
from datetime import datetime

def send_message(when, where, moviename, starttime):
  
  # 생성한 Slack 웹훅 주소
  hook = ''
  content = f":party-parrot-mal-mal: {when} {where} {moviename} {starttime} 메박 떴다"
  
  # 메시지 전송
  requests.post(
    hook,  
    json={
      'blocks': [
        {
          'type': 'section', 
          'text': {
            'type': 'mrkdwn',
            'text': content
          }
        }
      ]
    }
  )


url = 'https://www.megabox.co.kr/on/oh/ohc/Brch/schedulePage.do'

params = {"brchNo": "1351", 
          "brchNo1": "1351",
          "crtDe": "20230726",
          "detailType": "area",
          "firstAt": "N",
          "masterType": "brch",
          "playDe": "20230726"}

response = requests.post(url, params=params).json()


for i in response['megaMap']['movieFormList']:
    if (i['movieNo'] == '23048900') & (i['playStartTime'].startswith('19')):
        print(i)
        send_message(i['playDe'], i['brchNm'], i['movieNm'], i['playStartTime'])
        break
        
        
    