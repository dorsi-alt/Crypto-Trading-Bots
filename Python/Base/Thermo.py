from ThermoBrain import ThermoBrainDataAnalysis
from Birdeye import BirdeyeDataServices
from ThermoInit import ThermoBot
from Settings import ThermoSettings




token = '0xfEA9DcDc9E23a9068bF557AD5b186675C61d33eA'

Birdeye = BirdeyeDataServices(ThermoSettings['apiKey'], token)
ThermoBrain = ThermoBrainDataAnalysis(ThermoSettings)
Thermo = ThermoBot(Birdeye, ThermoBrain)
FilledPrice = Thermo.SeekEntry()

