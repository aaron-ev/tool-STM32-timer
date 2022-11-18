
import sys
import getopt

# timx_clk = 84000000; # Hz
# prescaler = 0;
# cnt_clk = timx_clk/(prescaler + 1) #Timer count clock
# time_base = 100 / 1000
# max_16bit_dec_value = 65535;
# period = time_base / (1 / cnt_clk);

class Stm32TimCalulator:
    defaultTimxClk = 16000000
    defaultPrescaler = 0
    maxCounterDecVal = 65535

    def __init__(self):
        pass

    def calculatePeriod(self, timxClk, period):
        print("Debug: Function {}".format(self.calculatePeriod.__name__))
        pass


def help():
    print("Debug: Function {}".format(help.__name__))
    print("\n\n\t\t\tAvailable commands:\n")
    print("\t" + "-t            TIMx CLK \n")
    print("\t" + "-f            Desired frequency\n")

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
            print("Debug: Desired frequency option")
            period = 1 / int(arg);
        elif option in ['h','--help']:
            print("Debug: Help option")
        else:
            print("Debug: else part")
            help()

    print("Debug: Results: timFreq = {}, period = {}".format(timFreq, period))

runApp()
# stm32Calculator =  Stm32TimCalulator()

# period = stm32Calculator.calculatePeriod(16000000, 0.1)
# print("Debug: Period calculater {}".format(period))

# timx_clk = 84000000; # Hz
# prescaler = 0;
# cnt_clk = timx_clk/(prescaler + 1) #Timer count clock
# time_base = 100 / 1000
# max_16bit_dec_value = 65535;
# period = time_base / (1 / cnt_clk);

# print("Debug: prescaler = {}, cnt_clk = {}, period = {}" .format(prescaler, cnt_clk, period))
# while (period > max_16bit_dec_value or not(str(period).endswith('.0'))):
#     prescaler = prescaler + 1
#     cnt_clk = timx_clk / (prescaler + 1) #Timer count clock
#     period = time_base / (1 / cnt_clk);
#     print("Debug: prescaler = {}, cnt_clk = {}, period = {}" .format(prescaler, cnt_clk, period))

# # print results
# print("Results: prescaler = {}, cnt_clk = {}, period = {}" .format(prescaler, cnt_clk, period))