from netmiko import ConnectHandler
from finderutils import finderutils

def findPortByMacAddress(protocol, address, port, username, password, secret, macAddress):
    if protocol == 'ssh':
        cisco_conn = {
        'device_type': 'ubiquiti_edgeswitch',
        'ip': address,
        'username': username,
        'password': password,
        'port': port,
        'secret': secret
        }
        try:
            net_connect = ConnectHandler(**cisco_conn)
            sysinfo = net_connect.send_command("show mac address-table | include {}".format(finderutils.formatMacAddressToCiscoSwitchFormat(macAddress)))
            if len(sysinfo.splitlines()) > 0:
                sysname = net_connect.send_command("show configuration | include hostname")
                description = net_connect.send_command("show version | include Model number")
                print(sysname.strip())
                print(description.strip())
                print(sysinfo.strip())
                print ('==============================================================================')
            else:
                pass
        except Exception as e:
            print(e)