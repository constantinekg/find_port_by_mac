# Initial devices db file
# Supported models of devices:
# edge: Edge switch
# cisco: Cisco switch
# mikrotikswos: Mikrotik switch

devices = [
    {'protocol':'ssh','user':'admin','password':'str0NGPWD!','address':'172.33.33.25','port':'22','devicetype':'cisco','secret':'str0NGPWD!'},
    {'protocol':'ssh','user':'admin','password':'str0NGPWD!','address':'172.33.33.26','port':'22','devicetype':'edge','secret':'str0NGPWD!'},
    {'protocol':'http','user':'admin','password':'str0NGPWD!','address':'172.33.33.27','port':'80','devicetype':'mikrotikswos','secret':''},
    {'protocol':'http','user':'admin','password':'str0NGPWD!','address':'172.33.33.28','port':'80','devicetype':'mikrotikswos','secret':''},
]