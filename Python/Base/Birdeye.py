import requests
import time

class BirdeyeDataServices:
    def __init__(self, Apikey, TokenAddress):
        self.Apikey = Apikey
        self.TokenAddress = TokenAddress
        self.headers =  {"x-chain": "base", "X-API-KEY": self.Apikey}

    def getTokenLivePrice(self):

        url = f"https://public-api.birdeye.so/defi/price?address={self.TokenAddress}"

        response = requests.get(url, headers=self.headers)

        print(response.text)

    def getTokenHistoricalPrice1m(self, lookBack):

        EndTime = int(time.time())
        StartTime = (EndTime  - (24*lookBack) * 60 * 60)
        url = f"https://public-api.birdeye.so/defi/history_price?address={self.TokenAddress}&address_type=token&type=1m&time_from={StartTime}&time_to={EndTime}"


        response = requests.get(url, headers=self.headers)

        print(response.text)
    
        




apikey = '6e0ffd19071a458c8af4ab121fa5e1e2'
token = '0x347F500323D51E9350285Daf299ddB529009e6AE'
Birdeye = BirdeyeDataServices(apikey, token)
Birdeye.getTokenLivePrice()
Birdeye.getTokenHistoricalPrice1m(2)

        
