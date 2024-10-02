#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from devices import edge
from devices import cisco
from devices import mikrotikswos
import devicesdb
from finderutils import finderutils
import argparse
import sys


parser = argparse.ArgumentParser(description='Find port by mac address')
parser.add_argument('-m','--mac', type=str, help='MAC address to find ex. B4:B0:24:F1:73:50')
args = parser.parse_args()

if args.mac == '' or args.mac == None or args.mac == ' ' or len(args.mac) < 2:
    print ('Please enter a valid mac address')
    sys.exit(1)

if __name__ == "__main__":
    for device in devicesdb.devices:
        match device['devicetype']:
            case 'edge':
                edge.findPortByMacAddress(device['protocol'], device['address'], device['port'], device['user'], device['password'], device['secret'], args.mac)
            case 'cisco':
                cisco.findPortByMacAddress(device['protocol'], device['address'], device['port'], device['user'], device['password'], device['secret'], args.mac)
            case 'mikrotikswos':
                mikrotikswos.findPortByMacAddress(device['protocol'], device['address'], device['port'], device['user'], device['password'], device['secret'], args.mac)
            case _:
                print ('Unknown device type')