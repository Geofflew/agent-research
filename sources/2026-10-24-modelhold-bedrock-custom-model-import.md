# Amazon Bedrock Custom Model Import (bring your own weights)

URL: https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html
Type: vendor
Read in session: 0008B

Summary: Customers can import their own customized open-architecture model weights (Mistral, Mixtral, etc.) into Bedrock and invoke them on demand, so the model version is the customer's. Doc explicitly names a financial-industry domain adaptation example. Limited to four regions; not usable with batch inference or CloudFormation.

Quotes:
- "proprietary model weights" — Bedrock Custom Model Import page
- "such as a financial industry wanting to create a model which generalizes well on pricing" — Bedrock Custom Model Import page, Adaptation pattern
- "Make sure that your import and use of the models in Amazon Bedrock complies with the terms or licenses applicable to the models." — Bedrock Custom Model Import page, note
- "Pretrained from scratch" — Bedrock Custom Model Import page, supported patterns
