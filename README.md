# helperScripts
helper scripts for various adhoc tasks in tpay backend

## Description of SignatureGenerator.py
- All the steps here follow [TravelokaPay-Uangku API Documentation - Generate API Signature](https://docs.google.com/document/d/1z6Yu_pDX9GSs5NFNfxz7wLCJuSdnK-QCuf1HvD0v-Fc/edit#)
- Make sure you have Python 3.7 or above
- How to use this script:
  1) Copy the script
  2) Change `requestBodyData` and `apiSecretKey` accordingly. You can get them from [parameter store](https://ap-southeast-1.console.aws.amazon.com/systems-manager/parameters/tvlk-secret/tpaycmw/pay/client-secret-prod/KpSi9x68HgG0BRr9qQwtyToUoXZQDTHlx/description?region=ap-southeast-1&tab=Table#list_parameter_filters=Name:Contains:KpSi9x68HgG0BRr9qQwtyToUoXZQDTHlx)
  3) Run `python SignatureGenerator.py` to get the signature

If all goes well, you should get this result <br/>
![image](https://user-images.githubusercontent.com/63224967/173758459-ab2c937d-c9c8-4d46-9447-e26299c4f8a8.png)
