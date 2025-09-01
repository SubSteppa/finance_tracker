# spy_price_today = "650"  # Variable showing price today (string)
# spy_price_yesterday = "640"  # Variable showing price yesterday (string)

# today = int(spy_price_today)  # using int to convert string to number
# yesterday = int(spy_price_yesterday)  # using int to convert string to number

# if today > yesterday:  # if else statements in in Python need : and to be indented
#     print('Spy is bullish')
# elif today < yesterday:
#     print('spy is bearish')


# spy_price_today = '650'
# spy_price_yesterday = '640'


# # Defining new variable "today" converting to floats for decimal
# today = float(spy_price_today)
# # Defining new variable "yesterday" converting to number for decimal
# yesterday = float(spy_price_yesterday)

# change_in_points = today - yesterday
# change_in_percentage = (change_in_points / yesterday) * 100

# if today > yesterday:
#     print(
#         f"Spy is bullish {change_in_points:.2f} points, {change_in_percentage:.2f}%")
# elif today < yesterday:
#     print(
#         f"Spy is bearish {change_in_points:.2f} points, {change_in_percentage:.2f}%")

# import yfinance as yf
# spy = yf.download("SPY", period='3d')

# if len(spy) < 3:
#     print("Not enough data to compare two days.")
# else:
#     yesterday = spy["Close"].iloc[-2].item()
#     today = spy["Close"].iloc[-1].item()

#     change_in_points = today - yesterday
#     change_in_percentage = (change_in_points / yesterday) * 100

#     if today > yesterday:
#         print(
#             f"SPY is bullish {change_in_points:.2f} points, {change_in_percentage:.2f}%")
#     elif today < yesterday:
#         print(
#             f"SPY is bearish {change_in_points:.2f} points, {change_in_percentage:.2f}%")
#     else:
#         print("SPY is neutral, no change.")

import yfinance as yf
# Imports the yfinance library to access stock/ETF data.
ticker = input('Enter Ticker Here').upper()
# Asks the user to enter a ticker symbol, converts to uppercase
data = yf.download(ticker, period='3d')
# Downloads last three days of ticker data

ticker = yf.Ticker(ticker)
# creaters ticker object for ticker entered
recent_changes = ticker.upgrades_downgrades
# grabs analylys upgrades/downgrades

yesterday = data["Close"].iloc[-2].item()
today = data["Close"].iloc[-1].item()

change_points = today - yesterday
change_percent = (change_points / yesterday) * 100

today_close_price = data["Close"].iloc[-1].item()
yesterdays_close_price = data["Close"].iloc[-2].item()

today_volume = data["Volume"].iloc[-1].item()
yesterday_volume = data["Volume"].iloc[-2].item()

# .iloc[-1] - last row (today’s close), .iloc[-2] - previous row (yesterday’s close)
# .item() - converts single value from pandas Series to a float (decimal).
# Change_points - absolute change in closing price from yesterday to today.
# Change_percent - percentage change relative to yesterday.
# Also storing today_close_price and yesterdays_close_price for display.

if today > yesterday:
    print(f"{ticker} is bullish ({ticker} closing price today was ${today_close_price:.2f}, +{change_points:.2f} points, +{change_percent:.2f}%)")
elif today < yesterday:
    print(f"{ticker} is bearish ({ticker} closing price today was ${today_close_price:.2f}, {change_points:.2f} points, {change_percent:.2f}%)")
else:
    print(f"{ticker} stayed the same (0.00 points, 0.00%)")

    # Compares today vs yesterday closing price.
    # Prints a message indicating bullish (up), bearish (down), or unchanged with the price, point change, and percent change.

print(f"Yesterdays Volume {yesterday_volume:,}")
print(f"Todays Volume {today_volume:,}")

if today_volume > yesterday_volume:
    print(f"Volume on {ticker} is higher today")
else:
    print(f"Volume on {ticker} is lower today")
if recent_changes is not None and recent_changes.empty:
    print(f"No recommendations for this ticker")
else:
    print(f"Here is the recommendations: {recent_changes}")

# Displays yesterday’s and today’s volume with comma formatting (:,) for readability.
# Compares volumes and prints whether today’s volume is higher or lower.


def human_readable(number):
    abs_num = abs(number)
    if abs_num >= 1_000_000_000_000:
        return f"${number/1_000_000_000_000:.2f}T"
    elif abs_num >= 1_000_000_000:
        return f"${number/1_000_000_000:.2f}B"
    elif abs_num >= 1_000_000:
        return f"${number/1_000_000:.2f}M"
    elif abs_num >= 1_000:
        return f"${number/1_000:.2f}K"
    else:
        return f"${number:.2f}"

# Converts large numbers into readable formats:
# Trillion → T
# Billion → B
# Million → M
# Thousand → K


rows_to_get = ["Basic EPS", "Diluted EPS", "Gross Profit"]
financials_data = {key: None for key in rows_to_get}

# Prepares a dictionary to hold financial values.
# Starts with None to handle cases where data is missing (like ETFs).

if ticker.income_stmt is not None and not ticker.income_stmt.empty:
    available_rows = [
        row for row in rows_to_get if row in ticker.income_stmt.index]
    if available_rows:
        financials = ticker.income_stmt.loc[available_rows]
        for row in available_rows:
            financials_data[row] = financials.loc[row].iloc[0]

# Checks if the income statement exists.
# Filters only the rows that exist (Basic EPS, Diluted EPS, Gross Profit).
# Stores values in financials_data dictionary.
# Prevents errors for tickers/ETFs that don’t have financials.

print(f"Basic EPS: ${financials_data['Basic EPS']:.2f}"
      if financials_data['Basic EPS'] is not None else "Basic EPS: N/A")
print(f"Diluted EPS: ${financials_data['Diluted EPS']:.2f}"
      if financials_data['Diluted EPS'] is not None else "Diluted EPS: N/A")
print(f"Gross Profit: {human_readable(financials_data['Gross Profit'])}"
      if financials_data['Gross Profit'] is not None else "Gross Profit: N/A")

# Prints EPS and Gross Profit in a neat readable fashion.
# Prints N/A if data not available (ETF's).
