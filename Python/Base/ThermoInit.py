import time
from Settings import ThermoSettings
import Display
class ThermoBot:
    def __init__(self, Birdeye, ThermoBrain):
        self.Birdeye = Birdeye
        self.ThermoBrain = ThermoBrain
        self.openPostionFlag = False

    def SeekEntry(self):
        while(self.openPostionFlag == False):
            historicalPrice1m = self.Birdeye.getTokenHistoricalPrice1m(1)
            historicalPrice3m = self.Birdeye.getTokenHistoricalPrice3m(1)
            historicalPrice5m = self.Birdeye.getTokenHistoricalPrice5m(1)

            RSI1m = self.ThermoBrain.CalulateRSI(historicalPrice1m)
            RSI3m = self.ThermoBrain.CalulateRSI(historicalPrice3m)
            RSI5m = self.ThermoBrain.CalulateRSI(historicalPrice5m)

            LastRSI1m, RSI1mBuySignal = self.ThermoBrain.analyzeRSI1m(RSI1m)
            LastRSI3m, RSI3mBuySignal = self.ThermoBrain.analyzeRSI3m(RSI3m)
            LastRSI5m, RSI5mBuySignal = self.ThermoBrain.analyzeRSI3m(RSI5m)

            print(LastRSI1m, LastRSI3m, LastRSI5m)

            buy = self.ThermoBrain.completeRSIBuySignal(RSI1mBuySignal, RSI3mBuySignal, RSI5mBuySignal)

            if buy:
                self.openPostionFlag = True
                FilledPrice = self.Birdeye.getTokenLivePrice()
                print('Buying Token')

            time.sleep(ThermoSettings['Sleep Time'])

        return FilledPrice
    
    def MonitoringTrade(self, filledPrice):
        TP, SL = self.ThermoBrain.getTPSL(filledPrice)
        while self.openPostionFlag:
            LivePrice =  self.Birdeye.getTokenLivePrice()
            PL = self.ThermoBrain.PercentageIncreaseCalc(LivePrice, filledPrice)
            displayMessage = f"Live Price: {LivePrice} Filled Price: {filledPrice} Take Profit: {TP} Stop Loss: {SL} PL: {PL}"
            print('\x1b[48;5;52m\x1b[K%s\x1b[0m', displayMessage)
            SellSignal = self.ThermoBrain.CheckOpenPosition(LivePrice, TP, SL)

            time.sleep(ThermoSettings['Sleep Time'])



        




