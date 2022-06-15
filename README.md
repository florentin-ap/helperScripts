# helperScripts
helper scripts for various adhoc tasks in TPAY backend, intended to reduce manual work

## Description for SignatureGenerator.py
- The steps here come from [TravelokaPay-Uangku API Documentation - Generate API Signature](https://docs.google.com/document/d/1z6Yu_pDX9GSs5NFNfxz7wLCJuSdnK-QCuf1HvD0v-Fc/edit#heading=h.gdj6me2ifrga)
- Get `prodSecretKey` from [parameter store](https://ap-southeast-1.console.aws.amazon.com/systems-manager/parameters/tvlk-secret/tpaycmw/pay/client-secret-prod/KpSi9x68HgG0BRr9qQwtyToUoXZQDTHlx/description?region=ap-southeast-1&tab=Table#list_parameter_filters=Name:Contains:KpSi9x68HgG0BRr9qQwtyToUoXZQDTHlx)
- How to use this:
  1) Make sure you have Python 3.7 or higher
  2) Copy this script
  3) Change `requestBodyData` and `apiSecretKey` as needed
  4) Run `python SignatureGenerator.py` in python environment
