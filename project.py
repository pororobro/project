import urllib.request
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import tqdm
import time
import random
# url정리 필요한 지역이 있으면 아래에 추가하면 됨
area = {
    '강남구 ': 'https://m.land.naver.com/cluster/ajax/articleList?view=atcl&cortarNo=1165010800&rletTpCd=OPST%3AVL%3AOR%3AGSW&tradTpCd=A1%3AB1%3AB2%3AB3&z=17&lat=37.4998395&lon=127.0273536&btm=37.495924&lft=127.0212542&top=37.5037548&rgt=127.0334529&pCortarNo=17_1165010800&addon=COMPLEX&bAddon=COMPLEX&isOnlyIsale=false'}
area_name = area.keys()
area_url = area.values()
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
# 네이버부동산 크롤링 함수
def land_info(area_name, area_url):
    info_df = pd.DataFrame()
    # url페이지를 range함수로 1~300까지 만들어서 for문 실행
    for i in tqdm.tqdm(range(1, 2)):
        try:
            # 강제로 실행을 멈춤 랜덤함수 사용 3초~7초 무작위 휴식
            time.sleep(random.randrange(3, 7))
            try:
                # 페이지 url생성
                url = area_url + '&page={}'.format(i)
                # 해더 정보 입력(봇이 아님을 인증)
                body = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36',
                }
                r = requests.get(url, headers=body)
                data = json.loads(r.text)
                # 페이지에 정보가 없을 경우 for문 break(매물정보는 1페이당 20개씩 있음)
                if data['more'] == False:
                    break
                else:
                    result = data['body']
                    df = pd.DataFrame(result)
                    info_df = info_df.append(df)
            # 요청할때 response가 없을 경우 60초 휴식후 재실행
            except requests.exceptions.Timeout:
                time.sleep(60)
                url = area_url + '&page={}'.format(i)
                print(url)
                body = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36',
                }
                r = requests.get(url, headers=body)
                data = json.loads(r.text)
                result = data['body']
                df = pd.DataFrame(result)
                info_df = info_df.append(df)
        # 키에러발생(정보가 없거나 오류발생)시 for문 종료
        except KeyError:
            print("KeyError : page {}".format(i))
            break
        # 제이슨파일로 업로드중 에러 발생시 10초 휴식후 재실행
        except JSONDecodeError:
            print("JSONDecodeError : page {}_sleep 10 sconds_restart".format(i))
            time.sleep(10)
            url = area_url + '&page={}'.format(i)
            body = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Whale/2.8.108.15 Safari/537.36',
            }
            r = requests.get(url, headers=body)
            data = json.loads(r.text)
            result = data['body']
            df = pd.DataFrame(result)
            info_df = info_df.append(df)
            # 데이터프레임 정리
    if info_df.empty:
        info_df = '매물정보 없음'
    else:
        # 컬럼정리
        info_df['지역명'] = area_name
        info_df = info_df[['cortarNo', '지역명', 'atclNo', 'vrfcTpCd', 'atclNm', 'bildNm', 'tradTpNm', 'rletTpNm', 'spc1',
                           'flrInfo', 'atclFetrDesc', 'atclCfmYmd', 'hanPrc', 'tagList', 'rltrNm', 'direction']]
        info_df = info_df.rename(
            columns={'cortarNo': '지역코드', 'atclNo': '매물코드', 'vrfcTpCd': '매물정보', 'atclNm': '단지명', 'bildNm': '동',
                     'tradTpNm': '매물방식', 'rletTpNm': '주거형태', 'spc1': '면적',
                     'flrInfo': '층', 'atclFetrDesc': '특이사항', 'atclCfmYmd': '확인매물', 'hanPrc': '거래가액',
                     'tagList': '태그', 'rltrNm': '부동산', 'direction': '매물방향'
                     })
    return info_df
total_df = pd.DataFrame()
for name, url in zip(area_name, area_url):
    try:
        time.sleep(random.randrange(1, 3))
        try:
            df = land_info(name, url)
            total_df = total_df.append(df)
        except requests.exceptions.Timeout:
            time.sleep(60)
            df = land_info(name, url)
            total_df = total_df.append(df)
    except KeyError:
        print("KeyError : {}".format(name))
        pass
total_df = total_df.drop_duplicates(['매물코드'])
total_df = total_df.set_index('매물코드')
print((total_df))
total_df