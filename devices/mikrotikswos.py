import requests
from finderutils import finderutils

def hex_to_string(hex_str):
    byte_values = bytes.fromhex(hex_str)
    result_string = byte_values.decode('utf-8')
    return result_string

def getMikrotikName(protocol, address, port, username, password):
    if protocol == 'http' or protocol == 'https':
        target_url = protocol + '://' + address + '/sys.b'
        try:
            res = requests.get(target_url, auth=requests.auth.HTTPDigestAuth(username, password), verify=False,  stream=True)
            return res.text
        except Exception as e:
            print(e)

def findPortByMacAddress(protocol, address, port, username, password, secret, macAddress):
    if protocol == 'http' or protocol == 'https':
        target_url = protocol + '://' + address + '/!dhost.b'
        try:
            res = requests.get(target_url, auth=requests.auth.HTTPDigestAuth(username, password), verify=False,  stream=True)
            allports = (res.text.replace('[','').replace(']','').replace('},{', '};{').split(sep=';'))
            for port in allports:
                portinfo = (port.split(','))
                macaddr = portinfo[0].replace('{adr:\'', '').replace('\'', '')
                vlanid = str(int(portinfo[1].replace('vid:', ''), 16))
                portnum = str(int(portinfo[2].replace('prt:', '').replace('}', ''), 16))
                if macaddr == macAddress.replace(':', '').lower():
                    print("mac: " + finderutils.formatMikrotikMacAddressToUpperCaseClassicAddress(macaddr), "vlan: " + vlanid, "port number: " + portnum)
                    res = getMikrotikName(protocol, address, port, username, password)
                    switchmodel = (hex_to_string(res.split(',')[4].replace('brd:', '').replace('\'', '')))
                    switchid = (hex_to_string(res.split(',')[6].replace('id:', '').replace('\'', '')))
                    print (switchmodel, switchid)
                    print ('==============================================================================')
        except Exception as e:
            print(e)