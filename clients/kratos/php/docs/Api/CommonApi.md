# Ory\Kratos\Client\CommonApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSchema**](CommonApi.md#getSchema) | **GET** /schemas/{id} | 
[**getSelfServiceBrowserLoginRequest**](CommonApi.md#getSelfServiceBrowserLoginRequest) | **GET** /self-service/browser/flows/requests/login | Get the request context of browser-based login user flows
[**getSelfServiceBrowserRegistrationRequest**](CommonApi.md#getSelfServiceBrowserRegistrationRequest) | **GET** /self-service/browser/flows/requests/registration | Get the request context of browser-based registration user flows
[**getSelfServiceBrowserSettingsRequest**](CommonApi.md#getSelfServiceBrowserSettingsRequest) | **GET** /self-service/browser/flows/requests/settings | Get the request context of browser-based settings flows
[**getSelfServiceError**](CommonApi.md#getSelfServiceError) | **GET** /self-service/errors | Get user-facing self-service errors
[**getSelfServiceVerificationRequest**](CommonApi.md#getSelfServiceVerificationRequest) | **GET** /self-service/browser/flows/requests/verification | Get the request context of browser-based verification flows



## getSchema

> object getSchema($id)



Get a traits schema definition

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new Ory\Kratos\Client\Api\CommonApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$id = 'id_example'; // string | ID must be set to the ID of schema you want to get

try {
    $result = $apiInstance->getSchema($id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonApi->getSchema: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **string**| ID must be set to the ID of schema you want to get |

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../../README.md#documentation-for-models)
[[Back to README]](../../README.md)


## getSelfServiceBrowserLoginRequest

> \Ory\Kratos\Client\Model\LoginRequest getSelfServiceBrowserLoginRequest($request)

Get the request context of browser-based login user flows

This endpoint returns a login request's context with, for example, error details and other information.  When accessing this endpoint through ORY Kratos' Public API, ensure that cookies are set as they are required for CSRF to work. To prevent token scanning attacks, the public endpoint does not return 404 status codes to prevent scanning attacks.  More information can be found at [ORY Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new Ory\Kratos\Client\Api\CommonApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request = 'request_example'; // string | Request is the Login Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/login?request=abcde`).

try {
    $result = $apiInstance->getSelfServiceBrowserLoginRequest($request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonApi->getSelfServiceBrowserLoginRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **string**| Request is the Login Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/login?request&#x3D;abcde&#x60;). |

### Return type

[**\Ory\Kratos\Client\Model\LoginRequest**](../Model/LoginRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../../README.md#documentation-for-models)
[[Back to README]](../../README.md)


## getSelfServiceBrowserRegistrationRequest

> \Ory\Kratos\Client\Model\RegistrationRequest getSelfServiceBrowserRegistrationRequest($request)

Get the request context of browser-based registration user flows

This endpoint returns a registration request's context with, for example, error details and other information.  When accessing this endpoint through ORY Kratos' Public API, ensure that cookies are set as they are required for CSRF to work. To prevent token scanning attacks, the public endpoint does not return 404 status codes to prevent scanning attacks.  More information can be found at [ORY Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new Ory\Kratos\Client\Api\CommonApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request = 'request_example'; // string | Request is the Registration Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/registration?request=abcde`).

try {
    $result = $apiInstance->getSelfServiceBrowserRegistrationRequest($request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonApi->getSelfServiceBrowserRegistrationRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **string**| Request is the Registration Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/registration?request&#x3D;abcde&#x60;). |

### Return type

[**\Ory\Kratos\Client\Model\RegistrationRequest**](../Model/RegistrationRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../../README.md#documentation-for-models)
[[Back to README]](../../README.md)


## getSelfServiceBrowserSettingsRequest

> \Ory\Kratos\Client\Model\SettingsRequest getSelfServiceBrowserSettingsRequest($request)

Get the request context of browser-based settings flows

When accessing this endpoint through ORY Kratos' Public API, ensure that cookies are set as they are required for checking the auth session. To prevent scanning attacks, the public endpoint does not return 404 status codes but instead 403 or 500.  More information can be found at [ORY Kratos User Settings & Profile Management Documentation](../self-service/flows/user-settings).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new Ory\Kratos\Client\Api\CommonApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request = 'request_example'; // string | Request is the Login Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/login?request=abcde`).

try {
    $result = $apiInstance->getSelfServiceBrowserSettingsRequest($request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonApi->getSelfServiceBrowserSettingsRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **string**| Request is the Login Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/login?request&#x3D;abcde&#x60;). |

### Return type

[**\Ory\Kratos\Client\Model\SettingsRequest**](../Model/SettingsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../../README.md#documentation-for-models)
[[Back to README]](../../README.md)


## getSelfServiceError

> \Ory\Kratos\Client\Model\ErrorContainer getSelfServiceError($error)

Get user-facing self-service errors

This endpoint returns the error associated with a user-facing self service errors.  When accessing this endpoint through ORY Kratos' Public API, ensure that cookies are set as they are required for CSRF to work. To prevent token scanning attacks, the public endpoint does not return 404 status codes to prevent scanning attacks.  More information can be found at [ORY Kratos User User Facing Error Documentation](https://www.ory.sh/docs/kratos/self-service/flows/user-facing-errors).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new Ory\Kratos\Client\Api\CommonApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$error = 'error_example'; // string | 

try {
    $result = $apiInstance->getSelfServiceError($error);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonApi->getSelfServiceError: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error** | **string**|  | [optional]

### Return type

[**\Ory\Kratos\Client\Model\ErrorContainer**](../Model/ErrorContainer.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../../README.md#documentation-for-models)
[[Back to README]](../../README.md)


## getSelfServiceVerificationRequest

> \Ory\Kratos\Client\Model\VerificationRequest getSelfServiceVerificationRequest($request)

Get the request context of browser-based verification flows

When accessing this endpoint through ORY Kratos' Public API, ensure that cookies are set as they are required for checking the auth session. To prevent scanning attacks, the public endpoint does not return 404 status codes but instead 403 or 500.  More information can be found at [ORY Kratos Email and Phone Verification Documentation](https://www.ory.sh/docs/kratos/selfservice/flows/verify-email-account-activation).

### Example

```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');


$apiInstance = new Ory\Kratos\Client\Api\CommonApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client()
);
$request = 'request_example'; // string | Request is the Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/verify?request=abcde`).

try {
    $result = $apiInstance->getSelfServiceVerificationRequest($request);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling CommonApi->getSelfServiceVerificationRequest: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **string**| Request is the Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/verify?request&#x3D;abcde&#x60;). |

### Return type

[**\Ory\Kratos\Client\Model\VerificationRequest**](../Model/VerificationRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints)
[[Back to Model list]](../../README.md#documentation-for-models)
[[Back to README]](../../README.md)

