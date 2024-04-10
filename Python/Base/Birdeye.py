import requests
import time
import pandas
import json

class BirdeyeDataServices:
    def __init__(self, Apikey, TokenAddress):
        self.Apikey = Apikey
        self.TokenAddress = TokenAddress
        self.headers =  {"x-chain": "base", "X-API-KEY": self.Apikey}

    def getTokenLivePrice(self):

        url = f"https://public-api.birdeye.so/defi/price?address={self.TokenAddress}"

        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        livePrice = parsed_data['data']['value']

        return livePrice

    def getTokenHistoricalPrice1m(self, TimeFrame):

        EndTime = int(time.time())
        StartTime = int((EndTime  - (24*TimeFrame) * 60 * 60))

        url = f"https://public-api.birdeye.so/defi/history_price?address={self.TokenAddress}&address_type=token&type=1m&time_from={StartTime}&time_to={EndTime}"


        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        df = pandas.DataFrame(parsed_data["data"]["items"])

        return df
    
    def getTokenHistoricalPrice3m(self, TimeFrame):

        EndTime = int(time.time())
        StartTime = int((EndTime  - (24*TimeFrame) * 60 * 60))

        url = f"https://public-api.birdeye.so/defi/history_price?address={self.TokenAddress}&address_type=token&type=3m&time_from={StartTime}&time_to={EndTime}"


        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        df = pandas.DataFrame(parsed_data["data"]["items"])

        return df
    
    def getTokenHistoricalPrice5m(self, TimeFrame):

        EndTime = int(time.time())
        StartTime = int((EndTime  - (24*TimeFrame) * 60 * 60))

        url = f"https://public-api.birdeye.so/defi/history_price?address={self.TokenAddress}&address_type=token&type=5m&time_from={StartTime}&time_to={EndTime}"

        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        df = pandas.DataFrame(parsed_data["data"]["items"])

        return df
    
    def getOHLCV1m(self, TimeFrame):
        EndTime = int(time.time())
        StartTime = (EndTime  - (24*TimeFrame) * 60 * 60)

        url = f"https://public-api.birdeye.so/defi/ohlcv?address={self.TokenAddress}&type=1m&time_from={StartTime}&time_to={EndTime}"

        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        df = pandas.DataFrame(parsed_data["data"]["items"])

        return df
    
    def getTokenOverview(self):

        url = f"https://public-api.birdeye.so/defi/token_overview?address={self.TokenAddress}"

        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        data = parsed_data['data']

        return data
    
    def getTokenSecurity(self):

        url = f"https://public-api.birdeye.so/defi/token_security?address={self.TokenAddress}"

        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        data = parsed_data['data']

        return data
    
    def getTokenSwaps(self, offset, limit):

        url = f"https://public-api.birdeye.so/defi/txs/token?address={self.TokenAddress}&offset={offset}&limit={limit}&tx_type=swap"

        response = requests.get(url, headers=self.headers)

        parsed_data = response.json()

        FilteredData = parsed_data['data']['items']

        FilteredData = FilteredData[0]

        # Gets quote, base, to, from and token price 
        return FilteredData
        
