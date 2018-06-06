"""
...TODO
"""

from com.modules import *

from argparse import ArgumentParser

parser = ArgumentParser(prog='ezPiC', conflict_handler='resolve')

parser.add_argument("-w", "--noweb",
                    dest="useWeb", default=G.CNF['useWeb'], action="store_false", 
                    help="Don't start web server part")
parser.add_argument("-W", "--useweb",
                    dest="useWeb", default=G.CNF['useWeb'], action="store_true", 
                    help="Start web server part")
                    
parser.add_argument("-i", "--noiot",
                    dest="useIoT", default=G.CNF['useIoT'], action="store_false", 
                    help="Don't start IoT part")
parser.add_argument("-I", "--useiot",
                    dest="useIoT", default=G.CNF['useIoT'], action="store_true", 
                    help="Start IoT part")
                    
parser.add_argument("-c", "--nocli",
                    dest="useCLI", default=G.CNF['useCLI'], action="store_false", 
                    help="Don't allow CLI commands")
parser.add_argument("-C", "--usecli",
                    dest="useCLI", default=G.CNF['useCLI'], action="store_true", 
                    help="Allow CLI commands")

parser.add_argument("-t", "--notelnet",
                    dest="useTelnet", default=G.CNF['useTelnet'], action="store_false", 
                    help="Don't allow Telnet commands")
parser.add_argument("-T", "--usetelnet",
                    dest="useTelnet", default=G.CNF['useTelnet'], action="store_true", 
                    help="Allow Telnet commands")

parser.add_argument("-l", "--loglevel", 
                    dest="logLevel", default=G.CNF['logLevel'], type=int, metavar="LEVEL",
                    help="Set the maximum logging level - 0=no output, 1=error, 2=warning, 3=info, 4=debug, 5=ext.debug")

parser.add_argument("-L", "--logfile", 
                    dest="logFile", default=G.CNF['logFile'], metavar="FILE",
                    help="Set FILE name for logging output")

parser.add_argument("-p", "--porttelnet", 
                    dest="portTelnet", default=G.CNF['portTelnet'], metavar='PORT', type=int,
                    help="Set the TCP port for telnet server")

parser.add_argument("-P", "--portweb", 
                    dest="portWeb", default=G.CNF['portWeb'], metavar='PORT', type=int,
                    help="Set the TCP port for web server")

parser.add_argument("-s", "--savecnf",
                    dest="saveCnf", default=False, action="store_true", 
                    help="Save actual configuration to file 'ezPiC.cnf'")

# TESTING
parser.add_argument("-q", "--quiet",
                    dest="verbose", default=True, action="store_false", 
                    help="don't print status messages to stdout")
parser.add_argument("-n", 
                    metavar='N', type=int,
                    help="print the N-th fibonacci number")
parser.add_argument("-x",
                    dest="x", default=10, type=int,
                    help="how many lines get printed")

args = parser.parse_args()

G.CNF['useWeb'] = args.useWeb
G.CNF['useIoT'] = args.useIoT
G.CNF['useCLI'] = args.useCLI
G.CNF['useTelnet'] = args.useTelnet
G.CNF['logLevel'] = args.logLevel
G.CNF['logFile'] = args.logFile
G.CNF['portTelnet'] = args.portTelnet
G.CNF['portWeb'] = args.portWeb

G.log(G.LOG_EXT_DEBUG, 'cnf: {}', G.CNF)

if args.saveCnf:
    with open('ezPiC.cnf', 'w') as f:
        json.dump(G.CNF, f, indent=0)
    
#######

