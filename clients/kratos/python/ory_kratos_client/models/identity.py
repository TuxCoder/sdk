# coding: utf-8

"""
    Ory Kratos

    Welcome to the ORY Kratos HTTP API documentation!  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ory_kratos_client.configuration import Configuration


class Identity(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'addresses': 'list[VerifiableAddress]',
        'id': 'str',
        'traits': 'object',
        'traits_schema_id': 'str',
        'traits_schema_url': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'id': 'id',
        'traits': 'traits',
        'traits_schema_id': 'traits_schema_id',
        'traits_schema_url': 'traits_schema_url'
    }

    def __init__(self, addresses=None, id=None, traits=None, traits_schema_id=None, traits_schema_url=None, local_vars_configuration=None):  # noqa: E501
        """Identity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._addresses = None
        self._id = None
        self._traits = None
        self._traits_schema_id = None
        self._traits_schema_url = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        self.id = id
        self.traits = traits
        self.traits_schema_id = traits_schema_id
        if traits_schema_url is not None:
            self.traits_schema_url = traits_schema_url

    @property
    def addresses(self):
        """Gets the addresses of this Identity.  # noqa: E501


        :return: The addresses of this Identity.  # noqa: E501
        :rtype: list[VerifiableAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this Identity.


        :param addresses: The addresses of this Identity.  # noqa: E501
        :type: list[VerifiableAddress]
        """

        self._addresses = addresses

    @property
    def id(self):
        """Gets the id of this Identity.  # noqa: E501


        :return: The id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Identity.


        :param id: The id of this Identity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def traits(self):
        """Gets the traits of this Identity.  # noqa: E501


        :return: The traits of this Identity.  # noqa: E501
        :rtype: object
        """
        return self._traits

    @traits.setter
    def traits(self, traits):
        """Sets the traits of this Identity.


        :param traits: The traits of this Identity.  # noqa: E501
        :type: object
        """
        if self.local_vars_configuration.client_side_validation and traits is None:  # noqa: E501
            raise ValueError("Invalid value for `traits`, must not be `None`")  # noqa: E501

        self._traits = traits

    @property
    def traits_schema_id(self):
        """Gets the traits_schema_id of this Identity.  # noqa: E501

        TraitsSchemaID is the ID of the JSON Schema to be used for validating the identity's traits.  # noqa: E501

        :return: The traits_schema_id of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._traits_schema_id

    @traits_schema_id.setter
    def traits_schema_id(self, traits_schema_id):
        """Sets the traits_schema_id of this Identity.

        TraitsSchemaID is the ID of the JSON Schema to be used for validating the identity's traits.  # noqa: E501

        :param traits_schema_id: The traits_schema_id of this Identity.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and traits_schema_id is None:  # noqa: E501
            raise ValueError("Invalid value for `traits_schema_id`, must not be `None`")  # noqa: E501

        self._traits_schema_id = traits_schema_id

    @property
    def traits_schema_url(self):
        """Gets the traits_schema_url of this Identity.  # noqa: E501

        TraitsSchemaURL is the URL of the endpoint where the identity's traits schema can be fetched from.  format: url  # noqa: E501

        :return: The traits_schema_url of this Identity.  # noqa: E501
        :rtype: str
        """
        return self._traits_schema_url

    @traits_schema_url.setter
    def traits_schema_url(self, traits_schema_url):
        """Sets the traits_schema_url of this Identity.

        TraitsSchemaURL is the URL of the endpoint where the identity's traits schema can be fetched from.  format: url  # noqa: E501

        :param traits_schema_url: The traits_schema_url of this Identity.  # noqa: E501
        :type: str
        """

        self._traits_schema_url = traits_schema_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Identity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Identity):
            return True

        return self.to_dict() != other.to_dict()
