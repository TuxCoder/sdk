# LoginRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **str** | and so on. | [optional] 
**expires_at** | **datetime** | ExpiresAt is the time (UTC) when the request expires. If the user still wishes to log in, a new request has to be initiated. | 
**forced** | **bool** | Forced stores whether this login request should enforce reauthentication. | [optional] 
**id** | **str** |  | 
**issued_at** | **datetime** | IssuedAt is the time (UTC) when the request occurred. | 
**methods** | [**dict(str, LoginRequestMethod)**](LoginRequestMethod.md) | Methods contains context for all enabled login methods. If a login request has been processed, but for example the password is incorrect, this will contain error messages. | 
**request_url** | **str** | RequestURL is the initial URL that was requested from ORY Kratos. It can be used to forward information contained in the URL&#39;s path or query for example. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


