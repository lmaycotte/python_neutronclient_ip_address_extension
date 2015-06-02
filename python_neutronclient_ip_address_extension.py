# Copyright 2015 Rackspace Hosting Inc.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from neutronclient.common import extension


class IPAddress(extension.NeutronClientExtension):
    resource = 'ip_address'
    resource_plural = '%ses' % resource
    object_path = '/%s' % resource_plural
    resource_path = '/%s/%%s' % resource_plural
    versions = ['2.0']


class IPAddressesList(extension.ClientExtensionList, IPAddress):
    shell_command = 'ip-address-list'
    list_columns = ['id', 'address', 'version', 'address_type', 'network_id',
                    'subnet_id', 'port_ids']


class IPAddressesCreate(extension.ClientExtensionCreate, IPAddress):
    shell_command = 'ip-address-create'


class IPAddressesUpdate(extension.ClientExtensionUpdate, IPAddress):
    shell_command = 'ip-address-update'


class IPAddressesDelete(extension.ClientExtensionDelete, IPAddress):
    shell_command = 'ip-address-delete'


class IPAddressesShow(extension.ClientExtensionShow, IPAddress):
    shell_command = 'ip-address-show'
