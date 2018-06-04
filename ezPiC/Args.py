"""
...TODO
"""

from com.modules import *

from argparse import ArgumentParser

parser = ArgumentParser()

# Add more options if you like
parser.add_argument("-f", "--file", 
                    dest="myFilenameVariable", metavar="FILE",
                    help="write report to FILE")
parser.add_argument("-q", "--quiet",
                    dest="verbose", default=True, action="store_false", 
                    help="don't print status messages to stdout")
parser.add_argument("-n", 
                    metavar='N', type=int,
                    help="print the N-th fibonacci number")
parser.add_argument("-x",
                    dest="x", default=10, type=int,
                    help="how many lines get printed")
parser.add_argument("-l", "--loglevel", 
                    dest="log_level", default=1, type=int,
                    help="set the logging level - 0=NoOutput, 1=Error, 2=Warning, 3=Info, 4=Debug, 5=Ext.Debug")

args = parser.parse_args()

print(args)

G.LOGLEVEL = args.log_level

#######

