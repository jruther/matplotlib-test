# Imported from http://www.opclabs.com/products/quickopc/languages-and-tools/python

import win32com.client

# Instantiate the client object 
client = win32com.client.Dispatch('OpcLabs.EasyOpc.DataAccess.EasyDAClient') 

# Perform the operation
value = client.ReadItemValue('', 'OPCLabs.KitServer.2', 'Demo.Single')

# Display results
print('value: ', value)

