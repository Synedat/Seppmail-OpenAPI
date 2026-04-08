# OpenAPI-YAML

This repo contains help files to help you use the SEPPmail API with Postman, a widely known REST-API client for Windows, Mac and Web.

## YAML File of the current API description

The current SEPPmail API release is always published on swagger.io. Here is is a copy to import your collection into postman.

The original can be found here:
<https://app.swaggerhub.com/apis-docs/SEPPmail/seppmail_rest_api>

## Sample Environment

When dealing with SEPPmail configs, it makes sense to store the access information at one place in postman. Environments are perfect for this, so every SEPPmail you want to talk to, has parameters like hostname, API Keys and so on.
These parameters are stored in environments. If you have different SEPPmails (multiple customers, or dev/test/prod environments) you can then easily switch between them by selecting a new environment in Postman.

A sample environment for import is stored in this file:

<https://github.com/seppmail/OpenAPI-YAML/blob/main/SEPPmail_Example.postman_environment>


## REST-Call initiazation script

To read the environment parameters and use them in your REST-CALL we wrote a little script which take the parameters from the environment and leverage them in the collection.

Use this script in the collections folder as pre-request-script

<https://github.com/seppmail/OpenAPI-YAML/blob/main/postmanConfig.js>


--- end of file ---
