import hmac
import hashlib

## list of apiSecretKeys ##
prodSecretKey = b""
stgSecretKey1 = b""
stgSecretKey2 = b""
dummyKey = b"vqPyVIpL5syJ5OawqJZkC73Mh9O7hg0l"

## input variables ##
requestBodyData = """{
    "externalCustomerInfo": {
        "externalCustomerId": "62816742232",
        "identityProvider": "uangku.co.id"
    },
    "currency": "IDR"
}"""
apiSecretKey = dummyKey

## functions to processs the keys ##
def removeNewlineTabAndSpace(requestBodyData):
    result = ''.join(requestBodyData.split())
    return result

def sha256(requestBodyDataProcessed):
    result = hashlib.sha256(requestBodyDataProcessed.encode('utf-8')).hexdigest()
    return result

def lowerCase (requestBodyDataProcessedSha256):
    result = requestBodyDataProcessedSha256.lower()
    return result

def hmac_sha256(stringToSign):
    result = hmac.new(apiSecretKey, msg=stringToSign.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
    return result

def getSignature(apiSecretKey,requestBodyData):
    requestBodyDataProcessed = removeNewlineTabAndSpace(requestBodyData)
    requestBodyDataProcessedSha256 = sha256(requestBodyDataProcessed)
    stringToSign = lowerCase(requestBodyDataProcessedSha256)
    signature = hmac_sha256(stringToSign).lower()
    print(signature)


getSignature(apiSecretKey,requestBodyData)