# CommonApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSchema**](CommonApi.md#getSchema) | **GET** /schemas/{id} | 
[**getSelfServiceBrowserLoginRequest**](CommonApi.md#getSelfServiceBrowserLoginRequest) | **GET** /self-service/browser/flows/requests/login | Get the request context of browser-based login user flows
[**getSelfServiceBrowserRegistrationRequest**](CommonApi.md#getSelfServiceBrowserRegistrationRequest) | **GET** /self-service/browser/flows/requests/registration | Get the request context of browser-based registration user flows
[**getSelfServiceBrowserSettingsRequest**](CommonApi.md#getSelfServiceBrowserSettingsRequest) | **GET** /self-service/browser/flows/requests/settings | Get the request context of browser-based settings flows
[**getSelfServiceError**](CommonApi.md#getSelfServiceError) | **GET** /self-service/errors | Get user-facing self-service errors
[**getSelfServiceVerificationRequest**](CommonApi.md#getSelfServiceVerificationRequest) | **GET** /self-service/browser/flows/requests/verification | Get the request context of browser-based verification flows


<a name="getSchema"></a>
# **getSchema**
> Object getSchema(id)



Get a traits schema definition

### Example
```java
// Import classes:
import sh.ory.kratos.ApiClient;
import sh.ory.kratos.ApiException;
import sh.ory.kratos.Configuration;
import sh.ory.kratos.models.*;
import sh.ory.kratos.api.CommonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommonApi apiInstance = new CommonApi(defaultClient);
    String id = "id_example"; // String | ID must be set to the ID of schema you want to get
    try {
      Object result = apiInstance.getSchema(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommonApi#getSchema");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID must be set to the ID of schema you want to get |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The raw identity traits schema |  -  |
**404** | genericError |  -  |
**500** | genericError |  -  |

<a name="getSelfServiceBrowserLoginRequest"></a>
# **getSelfServiceBrowserLoginRequest**
> LoginRequest getSelfServiceBrowserLoginRequest(request)

Get the request context of browser-based login user flows

This endpoint returns a login request&#39;s context with, for example, error details and other information.  When accessing this endpoint through ORY Kratos&#39; Public API, ensure that cookies are set as they are required for CSRF to work. To prevent token scanning attacks, the public endpoint does not return 404 status codes to prevent scanning attacks.  More information can be found at [ORY Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example
```java
// Import classes:
import sh.ory.kratos.ApiClient;
import sh.ory.kratos.ApiException;
import sh.ory.kratos.Configuration;
import sh.ory.kratos.models.*;
import sh.ory.kratos.api.CommonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommonApi apiInstance = new CommonApi(defaultClient);
    String request = "request_example"; // String | Request is the Login Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/login?request=abcde`).
    try {
      LoginRequest result = apiInstance.getSelfServiceBrowserLoginRequest(request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommonApi#getSelfServiceBrowserLoginRequest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **String**| Request is the Login Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/login?request&#x3D;abcde&#x60;). |

### Return type

[**LoginRequest**](LoginRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | loginRequest |  -  |
**403** | genericError |  -  |
**404** | genericError |  -  |
**410** | genericError |  -  |
**500** | genericError |  -  |

<a name="getSelfServiceBrowserRegistrationRequest"></a>
# **getSelfServiceBrowserRegistrationRequest**
> RegistrationRequest getSelfServiceBrowserRegistrationRequest(request)

Get the request context of browser-based registration user flows

This endpoint returns a registration request&#39;s context with, for example, error details and other information.  When accessing this endpoint through ORY Kratos&#39; Public API, ensure that cookies are set as they are required for CSRF to work. To prevent token scanning attacks, the public endpoint does not return 404 status codes to prevent scanning attacks.  More information can be found at [ORY Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example
```java
// Import classes:
import sh.ory.kratos.ApiClient;
import sh.ory.kratos.ApiException;
import sh.ory.kratos.Configuration;
import sh.ory.kratos.models.*;
import sh.ory.kratos.api.CommonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommonApi apiInstance = new CommonApi(defaultClient);
    String request = "request_example"; // String | Request is the Registration Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/registration?request=abcde`).
    try {
      RegistrationRequest result = apiInstance.getSelfServiceBrowserRegistrationRequest(request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommonApi#getSelfServiceBrowserRegistrationRequest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **String**| Request is the Registration Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/registration?request&#x3D;abcde&#x60;). |

### Return type

[**RegistrationRequest**](RegistrationRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | registrationRequest |  -  |
**403** | genericError |  -  |
**404** | genericError |  -  |
**410** | genericError |  -  |
**500** | genericError |  -  |

<a name="getSelfServiceBrowserSettingsRequest"></a>
# **getSelfServiceBrowserSettingsRequest**
> SettingsRequest getSelfServiceBrowserSettingsRequest(request)

Get the request context of browser-based settings flows

When accessing this endpoint through ORY Kratos&#39; Public API, ensure that cookies are set as they are required for checking the auth session. To prevent scanning attacks, the public endpoint does not return 404 status codes but instead 403 or 500.  More information can be found at [ORY Kratos User Settings &amp; Profile Management Documentation](../self-service/flows/user-settings).

### Example
```java
// Import classes:
import sh.ory.kratos.ApiClient;
import sh.ory.kratos.ApiException;
import sh.ory.kratos.Configuration;
import sh.ory.kratos.models.*;
import sh.ory.kratos.api.CommonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommonApi apiInstance = new CommonApi(defaultClient);
    String request = "request_example"; // String | Request is the Login Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/login?request=abcde`).
    try {
      SettingsRequest result = apiInstance.getSelfServiceBrowserSettingsRequest(request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommonApi#getSelfServiceBrowserSettingsRequest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **String**| Request is the Login Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/login?request&#x3D;abcde&#x60;). |

### Return type

[**SettingsRequest**](SettingsRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | settingsRequest |  -  |
**403** | genericError |  -  |
**404** | genericError |  -  |
**410** | genericError |  -  |
**500** | genericError |  -  |

<a name="getSelfServiceError"></a>
# **getSelfServiceError**
> ErrorContainer getSelfServiceError(error)

Get user-facing self-service errors

This endpoint returns the error associated with a user-facing self service errors.  When accessing this endpoint through ORY Kratos&#39; Public API, ensure that cookies are set as they are required for CSRF to work. To prevent token scanning attacks, the public endpoint does not return 404 status codes to prevent scanning attacks.  More information can be found at [ORY Kratos User User Facing Error Documentation](https://www.ory.sh/docs/kratos/self-service/flows/user-facing-errors).

### Example
```java
// Import classes:
import sh.ory.kratos.ApiClient;
import sh.ory.kratos.ApiException;
import sh.ory.kratos.Configuration;
import sh.ory.kratos.models.*;
import sh.ory.kratos.api.CommonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommonApi apiInstance = new CommonApi(defaultClient);
    String error = "error_example"; // String | 
    try {
      ErrorContainer result = apiInstance.getSelfServiceError(error);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommonApi#getSelfServiceError");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error** | **String**|  | [optional]

### Return type

[**ErrorContainer**](ErrorContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User-facing error response |  -  |
**403** | genericError |  -  |
**404** | genericError |  -  |
**500** | genericError |  -  |

<a name="getSelfServiceVerificationRequest"></a>
# **getSelfServiceVerificationRequest**
> VerificationRequest getSelfServiceVerificationRequest(request)

Get the request context of browser-based verification flows

When accessing this endpoint through ORY Kratos&#39; Public API, ensure that cookies are set as they are required for checking the auth session. To prevent scanning attacks, the public endpoint does not return 404 status codes but instead 403 or 500.  More information can be found at [ORY Kratos Email and Phone Verification Documentation](https://www.ory.sh/docs/kratos/selfservice/flows/verify-email-account-activation).

### Example
```java
// Import classes:
import sh.ory.kratos.ApiClient;
import sh.ory.kratos.ApiException;
import sh.ory.kratos.Configuration;
import sh.ory.kratos.models.*;
import sh.ory.kratos.api.CommonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommonApi apiInstance = new CommonApi(defaultClient);
    String request = "request_example"; // String | Request is the Request ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/verify?request=abcde`).
    try {
      VerificationRequest result = apiInstance.getSelfServiceVerificationRequest(request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommonApi#getSelfServiceVerificationRequest");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **String**| Request is the Request ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/verify?request&#x3D;abcde&#x60;). |

### Return type

[**VerificationRequest**](VerificationRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | verificationRequest |  -  |
**403** | genericError |  -  |
**404** | genericError |  -  |
**500** | genericError |  -  |

