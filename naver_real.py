import requests

def fetch_hellio(page):
    cookies = {
        'NAC': 'TNveD4gbQSn7B',
        'nhn.realestate.article.rlet_type_cd': 'A01',
        'nhn.realestate.article.trade_type_cd': '""',
        'nhn.realestate.article.ipaddress_city': '1100000000',
        '_fwb': '202kP0rt8BLi0hoIUSQH23C.1738941933424',
        'NACT': '1',
        'landHomeFlashUseYn': 'Y',
        'NNB': 'CPU7447OEWTGO',
        'SRT30': '1738941934',
        'SRT5': '1738941934',
        '_fwb': '202kP0rt8BLi0hoIUSQH23C.1738941933424',
        'REALESTATE': 'Sat%20Feb%2008%202025%2000%3A26%3A00%20GMT%2B0900%20(Korean%20Standard%20Time)',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ko;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3Mzg5NDE5NjAsImV4cCI6MTczODk1Mjc2MH0.yrE9CJCTInxiz7luHVL26TRk8pM60jb-DhXP7IGOP1c',
        # 'cookie': 'NAC=TNveD4gbQSn7B; nhn.realestate.article.rlet_type_cd=A01; nhn.realestate.article.trade_type_cd=""; nhn.realestate.article.ipaddress_city=1100000000; _fwb=202kP0rt8BLi0hoIUSQH23C.1738941933424; NACT=1; landHomeFlashUseYn=Y; NNB=CPU7447OEWTGO; SRT30=1738941934; SRT5=1738941934; _fwb=202kP0rt8BLi0hoIUSQH23C.1738941933424; REALESTATE=Sat%20Feb%2008%202025%2000%3A26%3A00%20GMT%2B0900%20(Korean%20Standard%20Time)',
        'priority': 'u=1, i',
        'referer': 'https://new.land.naver.com/complexes/111515?ms=37.497624,127.107268,17&a=APT:ABYG:JGC:PRE&e=RETAIL',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    response = requests.get(
        f'https://new.land.naver.com/api/articles/complex/111515?realEstateType=APT%3AABYG%3AJGC%3APRE&tradeType=&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={page}&complexNo=111515&buildingNos=&areaNos=&type=list&order=rank',
        cookies=cookies,
        headers=headers,
    )

    return response