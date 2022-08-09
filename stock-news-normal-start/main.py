import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "API KEY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "NEW API KEY"
TWILIO_SID = "TWILIO SID"
TWILIO_AUTH_TOKEN = "TWILIO AUTH"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_paramaters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_paramaters)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]

yesterday_closing_price = data_list[0]['4. close']

day_before_yday_closing_price = data_list[1]['4. close']

difference = abs(float(yesterday_closing_price) - float(day_before_yday_closing_price))

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

if abs(diff_percent) > 1:
    news_paramters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_paramters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    news_list = news_data[:3]
    formatted_article_list = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in
                              news_list]
    print(formatted_article_list)

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_article_list:
        message = client.messages \
            .create(
            body=article,
            from_='+13185089960',
            to='+447735989248'
        )

else:
    print("No news")

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

