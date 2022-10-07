'''Day 036 - This project is a stock news app which essentially can take stock codes, check if there are
significant changes in the stock price and then send a text message with the latest news articles if there
are. There was no real guidance with this project so it was I had to essentially figure out how to do all
the steps with the only guidance being APIs to use. And even then one of the APIs suggested doesn't work
in the UK so I had to find a new API and adjust the solution. It taught me a lot about reading through
AI documentation, and I also tried to use my knowledge of functions to make the program neater and also
reduce calling every API if it's not necessary (so 2 APIs only get called if there has been a significant
change in the stock price), which reduces the hammering of API calls.'''

from env_var import STOCK_API_KEY, NEWS_API_KEY, TEXT_API_KEY, TEXT_ACCOUNT_SID, TEXT_AUTH_TOKEN, TEXT_PHONE_NUMBER_SEND, TEXT_PHONE_NUMBER_RECEIVE
import requests
from twilio.rest import Client

# First lets store all the relevant environment variables
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
news_api_key = NEWS_API_KEY
phone_api = TEXT_API_KEY
account_sid = TEXT_ACCOUNT_SID
auth_token = TEXT_AUTH_TOKEN
phone_number_send = TEXT_PHONE_NUMBER_SEND
phone_number_receive = TEXT_PHONE_NUMBER_RECEIVE

# Then store all the params for the different APIs
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact",
    "datatype": "json"
}
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": news_api_key,
    "country": "gb, us, ie, ca, au",
    "language": "en",
}

#--------------------------------- FUNCTIONS --------------------------------------------------

# Function to call the news API
def news_api_call() -> dict:
    '''This function calls to the News API and gets the most recent 3 articles of the given stock
    to pass to the message function'''
    # Then lets try calling the API
    news_response = requests.get("https://newsdata.io/api/1/news", params=news_params)
    # Raise any errors
    news_response.raise_for_status()
    # Convert the response to JSON format
    news_data = news_response.json()
    # Then get the first 3 articles
    articles = news_data["results"][:3]
    # Store the data for the title, link and description of each data into an array of touples
    articles_data = [(article["title"], article["description"], article["link"]) for article in articles]
    # Then store the information into a dictionary of articles with an array of properties
    articles_dict = {
        "article_1": [articles_data[0][0], articles_data[0][1], articles_data[0][2]],
        "article_2": [articles_data[1][0], articles_data[1][1], articles_data[1][2]],
        "article_3": [articles_data[2][0], articles_data[2][1], articles_data[2][2]],
    }
    # Finally return articles dict
    return articles_dict

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
# First store all the necessary environment variables for twilio

# first use a function to take the news data and format it into a string
def format_news_data(results: dict, percentage_change: float, negative: bool) -> str:
    # Store the data
    article_1 = results["article_1"]
    article_2 = results["article_2"]
    article_3 = results["article_3"]
    # Make a formatted string to text
    return_string = f'''
    {STOCK}: {percentage_change}%{"🔺"*negative + "🔻"*(not negative)}

    Headline 1: {article_1[0]}
    Brief 1: {article_1[1]}
    Link 1: {article_1[2]}

    Headline 2: {article_2[0]}
    Brief 2: {article_2[1]}
    Link 2: {article_2[2]}

    Headline 3: {article_3[0]}
    Brief 3: {article_3[1]}
    Link 3: {article_3[2]}
    '''
    # Return the string
    return return_string

# Function to send the text message
def send_text_message(message_content: str):

    # Create a new client
    client = Client(account_sid, auth_token)
    # Send the message
    message = client.messages \
                .create(
                        body=message_content,
                        from_=phone_number_send,
                        to=phone_number_receive
                    )
    # Print the message sid
    print(message.sid)

# Function to call the stock API
def stock_api_call():
    # Lets try calling the API
    alpha_response = requests.get("https://www.alphavantage.co/query", params=alpha_params)
    # Raise any errors
    alpha_response.raise_for_status()
    # Convert the response to JSON format
    alpha_data = alpha_response.json()
    # Then get today and the previous days close prices
    dates = [dict for dict in alpha_data["Time Series (Daily)"].items()]
    today_close = float(dates[0][1]["4. close"])
    yesterday_close = float(dates[1][1]["4. close"])
    # Then calculate percentage change
    percentage_change = round(((today_close - yesterday_close) / yesterday_close * 100), 2)
    # Check if percentage change is positive or negative and store the result in a bool
    negative = percentage_change < 0
    # Then if the percentage change is greater than 5 we send a text message
    if abs(percentage_change) > 5:
        send_text_message(format_news_data(news_api_call(), percentage_change, negative))

#--------------------------------- MAIN --------------------------------------------------

stock_api_call()