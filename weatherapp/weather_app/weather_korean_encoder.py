def weather_korean_encoder(weather_id, rain, showers, month):
    weather_id = int(weather_id) if weather_id else 0
    rain = float(rain) if rain else 0
    showers = float(showers) if showers else 0

    seasonal_rain = ['(일비)', '(잠비)', '(떡비)', '(술비)']
    weather_type = ""
    
    if weather_id == 200:
        weather_type = "우레와 잔비 "

    elif weather_id == 201:
        weather_type = "우레와 비 "

    elif weather_id == 202:
        weather_type = "우레와 장대비 "
        
    elif weather_id == 210:
        weather_type = "얌전한 천둥과 번개"
    
    elif weather_id == 211:
        weather_type = "천둥과 번개"

    elif weather_id == 212:
        weather_type = "요란한 천둥과 번개"

    elif weather_id == 221:
        weather_type = "깔쭉깔쭉한 천둥과 번개"

    elif weather_id == 230:
        weather_type = "번개와 가랑비"

    elif weather_id == 231:
        weather_type = "번개와 이슬비"

    elif weather_id == 232:
        weather_type = "번개와 부슬비"

    elif weather_id == 300:
        weather_type = "안개비"

    elif weather_id == 301:
        weather_type = "보슬비"

    elif weather_id == 302:
        weather_type = "부슬비"

    elif weather_id == 310:
        weather_type = "이슬비"

    elif weather_id == 311:
        weather_type = "가랑비"

    elif weather_id == 312:
        weather_type = "잔비"

    elif weather_id == 313:
        weather_type = "소나기와 이슬비"

    elif weather_id == 314:
        weather_type = "세찬 소나기와 이슬비"

    elif weather_id == 321:
        weather_type = "실비"

    elif weather_id == 500:
        weather_type = "잔비"

    elif weather_id == 501:
        weather_type = "발비"

    elif weather_id == 502:
        weather_type = "작달비"

    elif weather_id == 503:
        weather_type = "장대비"

    elif weather_id == 504:
        weather_type = "억수"

    elif weather_id == 511:
        weather_type = "누리"

    elif weather_id == 520:
        weather_type = "여린 소나기"

    elif weather_id == 521:
        weather_type = "소나기"

    elif weather_id == 522:
        weather_type = "세찬 소나기"

    elif weather_id == 531:
        weather_type = "늘어지는 소나기"
    
    elif weather_id == 600:
        weather_type = "자국눈"

    elif weather_id == 601:
        weather_type = "마른눈"

    elif weather_id == 602:
        weather_type = "함박눈"

    elif weather_id == 611:
        weather_type = "진눈깨비"

    elif weather_id == 612:
        weather_type = "분분설"

    elif weather_id == 613:
        weather_type = "눈까비"

    elif weather_id == 615:
        weather_type = "여린 질눈"

    elif weather_id == 616:
        weather_type = "질눈"

    elif weather_id == 620:
        weather_type = "가루눈"

    elif weather_id == 621:
        weather_type = "소나기눈"

    elif weather_id == 622:
        weather_type = "발등눈"

    elif weather_id == 701:
        weather_type = "엷은 안개"

    elif weather_id == 711:
        weather_type = "연기"

    elif weather_id == 721:
        weather_type = "아지랑이"

    elif weather_id == 731:
        weather_type = "모래바람"

    elif weather_id == 741:
        weather_type = "안개"

    elif weather_id == 751:
        weather_type = "모래바람"

    elif weather_id == 761:
        weather_type = "먼지"

    elif weather_id == 762:
        weather_type = "화산재"

    elif weather_id == 771:
        weather_type = "돌풍"

    elif weather_id == 781:
        weather_type = "용수바람"

    elif weather_id == 800:
        weather_type = "맑음"

    elif weather_id == 801:
        weather_type = "구름 조금"

    elif weather_id == 802:
        weather_type = "구름 약간"

    elif weather_id == 803:
        weather_type = "구름 많음"

    elif weather_id == 804:
        weather_type = "흐림"
    

    if weather_id>=200 and weather_id<=531:
        if month in [12, 1, 2]:
            weather_type = weather_type + seasonal_rain[3]
        elif month in [3, 4, 5]:
            weather_type = weather_type + seasonal_rain[0]
        elif month in [6, 7, 8]:
            weather_type = weather_type + seasonal_rain[1]
        elif month in [9, 10, 11]:
            weather_type = weather_type + seasonal_rain[2]
        
    return weather_type
