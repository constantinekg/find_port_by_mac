from netmiko import ConnectHandler

def findPortByMacAddress(protocol, address, port, username, password, secret, macAddress):
    if protocol == 'ssh':
        edge_conn = {
        'device_type': 'ubiquiti_edgeswitch',
        'ip': address,
        'username': username,
        'password': password,
        'port': port,
        'secret': secret
        }
        try:
            net_connect = ConnectHandler(**edge_conn)
            sysinfo = net_connect.send_command("show mac-addr-table | include {}".format(macAddress.upper()))
            if len(sysinfo.splitlines()) > 0:
                sysname = net_connect.send_command("show sysinfo | include Name")
                description = net_connect.send_command("show sysinfo | include Description")
                print(sysname.strip())
                print(description.strip())
                print(sysinfo.strip())
                print ('==============================================================================')
            else:
                pass
        except Exception as e:
            print(e)