#########################################################
#   Author: Aaron Escoboza
#   Description: Calculate a the pulse value based
#                a given TIMx frequency and desired
#                channel frequency.
#########################################################

import sys
import getopt
import math
class Stm32TimCalulator:
    defaultTimxClk = 16000000
    defaultPrescaler = 0
    maxCounterDecVal = 65535

    def __init__(self):
        pass

    def calculatePulse(self, timxClk, desiredChannelPeriod):
        print("Debug: Function {}".format(self.calculatePulse.__name__))
        # Initial timer register values
        pulse = 0
        prescaler = 0
        time_base = (desiredChannelPeriod / 2) * 1000
        while (pulse > self.maxCounterDecVal or not(str(pulse).endswith('.0')) or (pulse == 0)):
            prescaler = prescaler + 1
            cnt_clk = float(timxClk) / (prescaler + 1) #Timer count clock
            pulse = time_base / (1 / cnt_clk);
            print("Debug: prescaler = {}, cnt_clk = {}, pulse = {}" .format(prescaler, cnt_clk, pulse))
        print("Results: Prescaler = {}, Pulse = {}".format(prescaler, pulse))

    def calculatePeriod(self, timxClk, prescaler, updateEventPeriod):
        prescaler = 0
        periodAutoReload = 0
        updateEventPeriod = float(updateEventPeriod) / 1000
        while True:
            print("Results: Prescaler = {}, Period = {}".format(prescaler, periodAutoReload))
            counterClk = float(timxClk) / (prescaler + 1)
            periodCounterClk = 1 / counterClk
            periodAutoReload = updateEventPeriod / periodCounterClk
            if ((periodAutoReload > 0) and (str(periodAutoReload).endswith('.0')) and (periodAutoReload < self.maxCounterDecVal)):
                break
            prescaler = prescaler + 1
        print("Results: Prescaler = {}, Period = {}".format(prescaler, periodAutoReload))

def help():
    print("Debug: Function {}".format(help.__name__))
    print("\n\n\t\t\tAvailable commands:\n")
    print("\t" + "-t            TIMx CLK \n")
    print("\t" + "-f            OC toggle mode: Desired channel frequency. Return pulse value\n")
    print("\t" + "-u            Base unit: Desired update event. Return period value")

def runApp():
    argv = sys.argv[1:]
    print("Debug: Function {}".format(runApp.__name__))

    try:
        options , args = getopt.getopt(argv, "t:f:h:l:u:")
    except:
        print("Internal error")

    print(options)
    print(args)
    for option, arg in options:
        if option in ['-t']:
            print("Debug: Option: Timer frequency option")
            timFreq = arg
        elif option in ['-f']:
            print("Debug: Option: Desired channel frequency")
            desiredChannelPeriod = 1 / float(arg);
        elif option in ['-u']:
            print("Debug: Option: Update event")
            updateEventPeriod = arg
        elif option in ['h','--help']:
            print("Debug: Help option")
        else:
            print("Debug: else part")
            help()

    calculator =  Stm32TimCalulator()
    # calculator.calculatePeriod(timFreq, 0, updateEventPeriod)
    calculator.calculatePulse(timFreq, desiredChannelPeriod)
    # print("Debug: Results: Timer frequency = {}, Desired channel period = {}".format(timFreq, desiredChannelPeriod))

runApp()