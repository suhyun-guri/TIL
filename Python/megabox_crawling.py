import requests
from bs4 import BeautifulSoup
import json, sys
from datetime import datetime

def send_message(when, where, moviename):
  
  # 생성한 웹훅 주소
  hook = '' # 웹훅 주소 
  content = f":party-parrot-mal-mal: {when} {where} {moviename} 메박 떴다"
  
  # 메시지 전송
  requests.post(
    hook,  
    json={
      'blocks': [
        {
          'type': 'section',  # 저는 메시지가 묶이지 않도록 section을 주로 사용합니다.
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
          "crtDe": "20230527",
          "detailType": "area",
          "firstAt": "N",
          "masterType": "brch",
          "playDe": "20230531"}

response = requests.post(url, params=params).json()


for i in response['megaMap']['movieFormList']:
    if i['movieNo'] == '23018401':
        # print(i)
        send_message(i['playDe'], i['brchNm'], i['movieNm'])
        break
    else:
        print(f"{datetime.now()} 없음")
        break
        
        
    