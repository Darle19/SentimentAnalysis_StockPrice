import pandas as pd
import requests
from textblob import TextBlob
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


def scale_sentiment(sentiment):
    """Scale the sentiment score to a 0-100 range."""
    return (sentiment + 1) * 50


def get_news_sentiment(company_name):
    news_data = []
    response = requests.get(f'https://newsapi.org/v2/everything?q={company_name}&language=en&apiKey=YourAPIKey')
    news_json = response.json()

    for article in news_json['articles']:
        title = article['title']
        description = article['description']
        content = f"{title}. {description}"

        blob = TextBlob(content)
        sentiment_score = scale_sentiment(blob.sentiment.polarity)

        news_data.append({
            'date': article['publishedAt'][:10],
            'sentiment': sentiment_score
        })

    # Convert the news data to a DataFrame
    sentiment_df = pd.DataFrame(news_data)
    sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])
    sentiment_df.set_index('date', inplace=True)
    sentiment_df = sentiment_df.resample('W').mean().reset_index()

    return sentiment_df


def get_stock_prices(ticker):
    # create a dummy stock price data
    dates = pd.date_range(start=datetime.now() - timedelta(days=730), end=datetime.now(), freq='W')
    close_prices = [100 + i * 0.2 for i in range(len(dates))]  # Генерация трендовых данных

    stock_data = pd.DataFrame({'date': dates.strftime('%Y-%m-%d'), 'Close': close_prices})
    return stock_data


def normalize_data(df):
    """Normalize with MinMaxScaler"""
    scaler = MinMaxScaler()
    df[['sentiment', 'Close']] = scaler.fit_transform(df[['sentiment', 'Close']])
    return df


def merge_and_analyze(company_name, ticker):
    sentiment_df = get_news_sentiment(company_name)
    stock_df = get_stock_prices(ticker)

    # Make sure both DataFrames have the same date format
    stock_df['date'] = pd.to_datetime(stock_df['date'])
    sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])

    merged_df = pd.merge(sentiment_df, stock_df, on='date', how='inner')

    # Normalizing the data
    merged_df = normalize_data(merged_df)

    correlation = merged_df['sentiment'].corr(merged_df['Close'])
    print(f"Correlation: {correlation}")

    # Визуализация
    plt.figure(figsize=(14, 7))
    plt.plot(merged_df['date'], merged_df['sentiment'], label='Normalized Sentiment Score')
    plt.plot(merged_df['date'], merged_df['Close'], label='Normalized Stock Price', color='orange')
    plt.xlabel('Date')
    plt.ylabel('Normalized Score / Price')
    plt.title(f'Normalized Sentiment and Stock Price Correlation for {company_name} over 2 Years (Weekly)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # save the data to a CSV file
    merged_df.to_csv(f'{company_name}_normalized_sentiment_vs_price.csv', index=False)

    return merged_df


# use the function to analyze the data
company_name = "Tesla"
ticker = "TSLA"
merged_data = merge_and_analyze(company_name, ticker)

# show the first few rows of the merged data
print(merged_data.head())
