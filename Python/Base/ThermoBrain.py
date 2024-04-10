import pandas

class ThermoBrainDataAnalysis:
    def __init__(self, settings):
        self.settings = settings
        pass

    def getTPSL(self, FilledPrice):
        StopLoss = FilledPrice * self.settings['Stop Loss']
        TakeProfit = FilledPrice * self.settings['Take Profit']

        return  TakeProfit, StopLoss
    
    def PercentageIncreaseCalc(self, CurrentPrice, FilledPrice):
        PercentIncrease = ((CurrentPrice - FilledPrice)/FilledPrice) * 100
        return PercentIncrease
    
    def CalulateRSI(self, historicalPrice):
        dataFrame = historicalPrice

        dataFrame['price_change'] = dataFrame['value'].diff()

        period = 14

        dataFrame['gain'] = dataFrame['price_change'].apply(lambda x: x if x > 0 else 0)
        dataFrame['loss'] = dataFrame['price_change'].apply(lambda x: abs(x) if x < 0 else 0)

        dataFrame['avg_gain'] = dataFrame['gain'].rolling(window=period).mean()
        dataFrame['avg_loss'] = dataFrame['loss'].rolling(window=period).mean()


        dataFrame['rs'] = dataFrame['avg_gain'] / dataFrame['avg_loss']

        dataFrame['rsi'] = 100 - (100 / (1 + dataFrame['rs']))

        return dataFrame['rsi']
    

    def analyzeRSI1m(self, RSI1):
        buySignal = False
        lastRSI1m = RSI1.iloc[-1]
        
        if(lastRSI1m < self.settings['RSI1m Boundry']):
            buySignal = True
        

        return lastRSI1m, buySignal
    
    def analyzeRSI3m(self, RSI3):
        buySignal = False
        lastRSI3m = RSI3.iloc[-1]
        
        if(lastRSI3m < self.settings['RSI3m Boundry']):
            buySignal = True
        
        return lastRSI3m, buySignal
    
    def analyzeRSI3m(self, RSI5):
        buySignal = False
        lastRSI5m = RSI5.iloc[-1]
        
        if(lastRSI5m < self.settings['RSI5m Boundry']):
            buySignal = True
        
        return lastRSI5m, buySignal
    
    def completeRSIBuySignal(self, RSI1Signal, RSI3Signal, RSI5Signal):
        buy = False
        if RSI1Signal:
            if RSI3Signal:
                if RSI5Signal:
                    buy = True
        
        return buy

    def CheckOpenPosition(self, LivePrice, TP, SL):
        sellSignal = False
        if LivePrice >= TP:
            sellSignal = True
        if LivePrice <= SL:
            sellSignal = True
        return sellSignal





