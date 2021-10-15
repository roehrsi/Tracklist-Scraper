"""
Created on 04.01.2020

@author: Daniel
"""

from src import tl_ndr, tl_harmony, tl_njoy
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("station", help="The station to scrape",
                    choices=["harmony", "ndr1nds", "ndr2", "njoy", "ndr903", "ndr1WN", "ndrRMV", "ndrkultur",
                             "ndrblue"])

# parser.add_argument("--spotify", nargs=3, metavar=("USER","PW","PLNAME"), help="WIP: Optionally provide spotify username and password to push scraped tracks into a plalist. Third argument is the desired name for the playlist. Playlists will be private.")

args = parser.parse_args()

if __name__ == '__main__':

    if args.station == "harmony":
        tl_harmony.run()
    elif args.station == "njoy":
        tl_njoy.run()
    elif args.station == "ndr1nds":
        tl_ndr.run(args.station)
    elif args.station == "ndr2":
        tl_ndr.run(args.station)
    elif args.station == "ndr903":
        tl_ndr.run(args.station)
    elif args.station == "ndr1WN":
        tl_ndr.run(args.station)
    elif args.station == "ndrRMV":
        tl_ndr.run(args.station)
    elif args.station == "ndrkultur":
        tl_ndr.run(args.station)
    elif args.station == "ndrblue":
        tl_ndr.run(args.station)
