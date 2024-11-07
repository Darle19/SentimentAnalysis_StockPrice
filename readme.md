
# Sentiment Analysis and Stock Price Correlation

This project analyzes the correlation between public sentiment and stock prices using Python. The script gathers news data, calculates sentiment scores, and matches these scores against historical stock prices to identify potential relationships over a two-year period with weekly granularity. The results include normalized visualizations and correlation analysis.

## Features
- **Sentiment Analysis**: Collects news articles and evaluates sentiment scores using `TextBlob`.
- **Stock Price Data**: Gathers weekly stock closing prices for a two-year period.
- **Data Normalization**: Normalizes both sentiment scores and stock prices for easy comparison.
- **Correlation Calculation**: Measures the correlation between sentiment and stock price movement.
- **Visualization**: Plots a graph comparing normalized sentiment and stock prices over time.
- **CSV Export**: Saves the merged data to a CSV file for further analysis.

## Requirements
- Python 3.x
- Libraries:
  - `pandas`
  - `requests`
  - `TextBlob`
  - `yfinance` (optional for real stock data)
  - `matplotlib`
  - `scikit-learn`

## Installation

Install the required Python libraries:
   ```bash
    pip install pandas requests textblob yfinance matplotlib scikit-learn
   ```

## Usage

1. Replace `YOUR_API_KEY` with your API key from [NewsAPI](https://newsapi.org/).
2. Run the script to analyze sentiment and stock prices:

   ```bash
   python main.py
   ```

## Example Output

- **Graph**: A plot comparing normalized sentiment scores and stock prices.
- **Correlation**: A correlation coefficient displayed in the console.
- **CSV File**: A CSV file with merged data is exported for further analysis.

## Future Enhancements

- Integration of social media sentiment (e.g., Twitter).
- Inclusion of additional financial metrics such as trading volume.
- Support for other data sources and regional filtering.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check out the [issues page](https://github.com/darle19/sentiment-stock-analysis/issues).

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or issues, please reach out via [email](mailto:your.cencet.99@gmail.com) or open an issue on GitHub.
