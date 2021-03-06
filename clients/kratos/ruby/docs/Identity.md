# OryHydraClient::Identity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addresses** | [**Array&lt;VerifiableAddress&gt;**](VerifiableAddress.md) |  | [optional] 
**id** | **String** |  | 
**traits** | [**Object**](.md) |  | 
**traits_schema_id** | **String** | TraitsSchemaID is the ID of the JSON Schema to be used for validating the identity&#39;s traits. | 
**traits_schema_url** | **String** | TraitsSchemaURL is the URL of the endpoint where the identity&#39;s traits schema can be fetched from.  format: url | [optional] 

## Code Sample

```ruby
require 'OryHydraClient'

instance = OryHydraClient::Identity.new(addresses: null,
                                 id: null,
                                 traits: null,
                                 traits_schema_id: null,
                                 traits_schema_url: null)
```


