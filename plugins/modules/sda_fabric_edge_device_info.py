#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_edge_device_info
short_description: Information module for Sda Fabric Edge Device
description:
- Get all Sda Fabric Edge Device.
version_added: '1.0.0'
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceIPAddress:
    description:
    - DeviceIPAddress query parameter. Device IP Address.
    type: str
requirements:
- dnacentersdk
seealso:
# Reference by Internet resource
- name: Sda Fabric Edge Device reference
  description: Complete reference of the Sda Fabric Edge Device object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sda Fabric Edge Device
  cisco.dnac.sda_fabric_edge_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    deviceIPAddress: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "name": "string",
      "roles": [
        "string"
      ],
      "deviceManagementIpAddress": "string",
      "siteHierarchy": "string"
    }
"""