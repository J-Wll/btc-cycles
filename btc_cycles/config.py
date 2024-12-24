
import datetime as datetime

# dates for coins in the top 10 that aren't stable
# just grabbed the first date I saw in the cmc all graph, not the most accurate but this is for the big picture anyway
# Bitcoin (BTC) =  (2009, 1, 3)
# Ethereum (ETH) = (2015, 8, 8)
# XRP =            (2013, 8, 5)
# BNB =            (2017, 7, 26)
# Solana (SOL) =   (2020, 4, 11)
# DOGE =           (2013, 12, 16)
# Cardano (ADA) =  (2017, 10, 2)
# Tron (TRX) =     (2017, 9, 30)

# eth usd example config
# self.token = "ETH"
# self.startDate = dt.datetime(2015, 8, 8)
# self.tokenName = "Ethereum"
# self.currency = "USD"


# used to fetch data
token = "ETH"
start_date = datetime.datetime(2015, 8, 8)
# used in the graph 
token_name = "Ethereum"
# used for both
currency = "USD"

time_now = datetime.datetime.today().strftime('%Y-%m-%d %H-%M-%S')

    
