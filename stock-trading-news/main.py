# __________________________STOCK TRADING NEWS ALERT_____________________________ #
# Searches for users stock of choice and sees if it has increased or decreased by 5% since yesterday.
# If so, it retrieves the top 3 most important articles about that stock.
# The program then texts the user the stock percent change and the title and summary of each article.

import requests
from twilio.rest import Client
from datetime import date, timedelta
STOCK = "TSLA"
COMPANY_NAME = "Tesla"


# __________________________SEND TWILIO TEXT MESSAGE_____________________________ #
def send_text(articles, percent):
    arrow = ""
    if percent > 0:
        arrow = "🔺"
    elif percent < 0:
        arrow = "🔻"
    account_sid = "ACCOUNT_SID"
    auth_token = "AUTH_TOKEN"

    if len(articles) == 0:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}: {arrow}{percent}%\n",
            from_='TWILIO NUMBER',
            to='USER NUMBER'
        )
            
    else:
        client = Client(account_sid, auth_token)
        for article in articles:
            message = client.messages.create(
                body=f"{STOCK}: {arrow}{percent}%\n"
                     f"{article}",
                from_='TWILIO NUMBER',
                to='USER NUMBER'
            )


# __________________________GET NEWS API DATA_____________________________ #
def get_news(percent):
    final_articles = []
    news_api_key = "NEWS_API_KEY"
    news_api_parameters = {
        "apikey": news_api_key,
        "q": COMPANY_NAME,
        "language": "en"
    }

    news_response = requests.get(url="https://newsapi.org/v2/top-headlines", params=news_api_parameters)
    news_data = news_response.json()

    if len(news_data["articles"]) == 0:
        final_articles = []
        send_text(final_articles, percent)
        return
    elif len(news_data["articles"]) < 3:
        articles = news_data["articles"][:len(news_data["articles"]) - 1]
    else:
        articles = news_data["articles"][:3]

    final_articles = [f"Headline: {article['title']} Brief: {article['description']}" for article in articles]

    send_text(final_articles, percent)


# __________________________GET ALPHA VANTAGE API DATA_____________________________ #
alpha_vantage_key = "ALPHA VANTAGE KEY"
alpha_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": alpha_vantage_key
}

response = requests.get(url="https://www.alphavantage.co/query", params=alpha_parameters)
data = response.json()

today = date.today()
yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

price_yesterday = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
price_day_before = float(data["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

percent_change = round(((price_yesterday-price_day_before)/price_yesterday)*100)

if percent_change >= 5 or percent_change <= -5:
    get_news(percent_change)
