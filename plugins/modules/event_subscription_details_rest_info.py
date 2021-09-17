#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_details_rest_info
short_description: Information module for Event Subscription Details Rest
description:
- Get all Event Subscription Details Rest.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  connectorType:
    description:
    - ConnectorType query parameter. Connector Type REST.
    type: str
  name:
    description:
    - Name query parameter. Name of the specific configuration.
    type: str
  instanceId:
    description:
    - InstanceId query parameter. Instance Id of the specific configuration.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Event Subscription Details Rest reference
  description: Complete reference of the Event Subscription Details Rest object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Event Subscription Details Rest
  cisco.dnac.event_subscription_details_rest_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    connectorType: string
    name: string
    instanceId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "instanceId": "string",
        "name": "string",
        "description": "string",
        "connectorType": "string",
        "url": "string",
        "method": "string",
        "trustCert": "string",
        "headers": [
          {
            "name": "string",
            "value": "string"
          }
        ],
        "queryParams": [
          "string"
        ],
        "pathParams": [
          "string"
        ]
      }
    ]
"""