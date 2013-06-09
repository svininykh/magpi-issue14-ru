"""
W. H. Bell <W.Bell@cern.ch>

A program to launch a BatchCalculatorClient on a pbs batch node.  The process
starts as a pbs job and then repeatly tries to connect back to the 
server process for instructions.  Jobs should be lauched by using a
script of the form:
  ../scripts/submitClients.sh 
"""

from FunctionCalculator import BatchCalculatorClient 

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        sys.stderr.write("  Usage: " + sys.argv[0] + " <server> <port> \n")
        sys.exit(1)
        
    client = BatchCalculatorClient(sys.argv[1], sys.argv[2])
    client.loop()
