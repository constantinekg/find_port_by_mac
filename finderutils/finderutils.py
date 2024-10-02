def formatMacAddressToCiscoSwitchFormat(macAddress):
    try:
        ciscomacformated = ''
        splitedmac = macAddress.split(':')
        ciscomacformated += splitedmac[0] + splitedmac[1] + '.' + splitedmac[2] + splitedmac[3] + '.' + splitedmac[4] + splitedmac[5]
        return ciscomacformated.lower()
    except:
        print('Error: Invalid mac address, trying to search by portial as:', macAddress.lower().replace(':',''))
        return macAddress.lower().replace(':','')
    finally:
        pass

def formatMikrotikMacAddressToUpperCaseClassicAddress(macAddress):
    formatedmac = []
    for i in range (0, len(list(macAddress)), 2):
        formatedmac.append(macAddress[i:i+2])
    return (':'.join(formatedmac))