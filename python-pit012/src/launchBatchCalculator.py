"""
W. H. Bell <W.Bell@cern.ch>

"""

import time
from FunctionCalculator import BatchCalculator

if __name__ == "__main__":

    # Create a batch calculator instance for parallel 
    # processing with many PCs.
    calculator = BatchCalculator("192.168.1.11", 20000)
    calculator.initialise()

    time.sleep(60) # Sleep for a minute to allow client server tests. 

    # Tell any clients connected to the batch calculator
    # server to shutdown and then shutdown server.
    calculator.shutdown()
