## Find port by mac address

### Description
This script will find the port number of a device by its mac address. It will use the devicesdb.py file to get the list of devices and their credentials. It will then use the finder.py main function to get the name of the device and find the port number of the device.

Supported devices:
- Cisco
- Mikrotik SWOS
- Edge switch

### Usage
```
source venv/bin/activate
./finder.py -m 00:e0:4c:38:03:05
```

### Sample output:
```
hostname SomeSW004-ASWCp-2F-48-01
Model number                    : WS-C2960-48PST-S
123    00e0.4c36.0105    DYNAMIC     Gi0/3
==============================================================================
System Name.................................... SomeSW004-DSWUp-48-01
System Description............................. EdgeSwitch 48 500W, 1.9.2, Linux 3.6.5-03329b4a, 1.2.0.5192732
123      00:E0:4C:38:03:05   3/3                    68       Learned
==============================================================================
mac: 00:e0:4c:38:03:05 vlan: 123 port number: 20
CSS326-24G-2S+ SomeSW-DSWM-1F-24-01
==============================================================================
mac: 00:e0:4c:38:03:05 vlan: 123 port number: 2
CSS326-24G-2S+ SomeSW-ASWM-2F-24-01
==============================================================================
```

### Requirements
- Python 3.8
- Paramiko
- requests
- netmiko
- json

version 1.0.0
- Added support for Mikrotik SWOS
- Added support for Edge switch
- Added support for Cisco devices