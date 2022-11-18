#########################################################
#   Author: Aaron Escoboza
#   Description: Calculate a the pulse value based
#                a given TIMx frequency and desired
#                channel frequency.
#########################################################

import sys
import getopt

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
            print("Debug: prescaler = {}, cnt_clk = {}, period = {}" .format(prescaler, cnt_clk, pulse))
        print("Results: Prescaler = {}, Pulse = {}".format(prescaler, pulse))


def help():
    print("Debug: Function {}".format(help.__name__))
    print("\n\n\t\t\tAvailable commands:\n")
    print("\t" + "-t            TIMx CLK \n")
    print("\t" + "-f            Desired channel frequency\n")

def runApp():
    argv = sys.argv[1:]
    print("Debug: Function {}".format(runApp.__name__))

    try:
        options , args = getopt.getopt(argv, "t:f:h:l:")
    except:
        print("Internal error")

    print(options)
    print(args)
    for option, arg in options:
        if option in ['-t']:
            print("Debug: Timer frequency option")
            timFreq = arg
        elif option in ['-f']:
            print("Debug: Desired channel frequency")
            desiredChannelPeriod = 1 / float(arg);
        elif option in ['h','--help']:
            print("Debug: Help option")
        else:
            print("Debug: else part")
            help()

    calculator =  Stm32TimCalulator()
    calculator.calculatePulse(timFreq, desiredChannelPeriod)
    print("Debug: Results: Timer frequency = {}, Desired channel period = {}".format(timFreq, desiredChannelPeriod))

runApp()