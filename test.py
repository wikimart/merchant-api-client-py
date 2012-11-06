from merchantapi_client import *

mapi = MerchantAPI("merchant-api-test.lan", "13491868046632", "FgVHxZrdzzXhKVW5gECGTg")
response = mapi.methodGetOrderList(10, 1) 

print response.getHttpCode()
print response.getError()
print response.getData()

