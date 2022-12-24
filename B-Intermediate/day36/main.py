import os
import requests

from datetime import datetime, timedelta

STOCK = 'TSLA'
COMPANY_NAME = 'Tesla'
AV_API_KEY = os.environ.get('ALPHAVANTAGE_API_KEY')

base_date = datetime.now()
start_date = base_date.replace(hour=20, minute=0, second=0, microsecond=0) - timedelta(days=3)
end_date = base_date.replace(hour=20, minute=0, second=0, microsecond=0) - timedelta(days=2)

print(start_date)
print(end_date)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").



av_params = {
    'function': 'TIME_SERIES_INTRADAY',
    'symbol': STOCK,
    'interval': '60min',
    'apikey': AV_API_KEY
}

url = 'https://www.alphavantage.co/query'
response = requests.get(url, params=av_params)
full_response = response.json()
stock_data = full_response[f'Time Series ({av_params["interval"]})']

start_price = float(stock_data[str(start_date)]['4. close'])
end_price = float(stock_data[str(end_date)]['4. close'])

dif_amount = start_price - end_price
dif_percent = dif_amount/start_price

# print(dif_percent)


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if dif_percent >= 0.05:

    NEWS_API_KEY = os.environ.get('NEWSAPI_API_KEY')

    news_params = {
        'q': f'+{COMPANY_NAME}',
        'searchIn': 'title',
        'from': start_date.date(),
        'to': end_date.date(),
        'sortBy': 'popularity',
        'apiKey': NEWS_API_KEY
    }

    url = 'https://newsapi.org/v2/everything'
    response = requests.get(url, params=news_params)
    full_response = response.json()
    top_3_articles = full_response['articles'][:3]
    # print(top_3_articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

    from twilio.rest import Client

    TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
    sender_phone = os.environ.get('TWILIO_SENDER_PHONE')
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')

    message_body = f'''
        {STOCK}: 🔺{int(dif_percent*100)}%
        Headline: {top_3_articles[1]['title']}?. 
        Brief: {top_3_articles[1]['description']}
        -----
        Headline: {top_3_articles[2]['title']}?. 
        Brief: {top_3_articles[2]['description']}
    '''

    client = Client(account_sid, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        messaging_service_sid='test',
        body=message_body,
        to='+50688888888' #REPLACE WITH REAL NUMBER
    )

    print(message.sid)
