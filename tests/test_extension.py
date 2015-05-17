import mock

from neutronclient import shell
from neutronclient.tests.unit import test_cli20

import python_neutronclient_ip_address_extension as ip_address


class FixtureExtensionLoader(test_cli20.CLITestV20Base):
    def setUp(self):
        # need to mock before super because extensions loaded on instantiation
        self._mock_extension_loading()
        super(FixtureExtensionLoader, self).setUp()

    def _create_patch(self, name, func=None):
        patcher = mock.patch(name)
        thing = patcher.start()
        self.addCleanup(patcher.stop)
        return thing

    def _mock_extension_loading(self):
        ext_pkg = 'neutronclient.common.extension'
        contrib = self._create_patch(ext_pkg + '._discover_via_entry_points')
        contrib.return_value = [("ip_address", ip_address)]
        return contrib


class TestShell(FixtureExtensionLoader):
    def test_ext_cmd_loaded(self):
        shell.NeutronShell('2.0')
        ext_cmd = {'ip-address-list': ip_address.IPAddressesList,
                   'ip-address-create': ip_address.IPAddressesCreate,
                   'ip-address-update': ip_address.IPAddressesUpdate,
                   'ip-address-show': ip_address.IPAddressesShow,
                   'ip-address-delete': ip_address.IPAddressesDelete}
        self.assertDictContainsSubset(ext_cmd, shell.COMMANDS['2.0'])

    def test_ip_address_create(self):
        pass

    def test_ip_addresses_list(self):
        pass

    def test_ip_address_show(self):
        pass

    def test_ip_address_update(self):
        pass

    def test_ip_address_delete(self):
        pass


class TestClient(FixtureExtensionLoader):
    def setUp(self):
        super(TestClient, self).setUp()
        self.resp = test_cli20.MyResp(200)

    def test_ip_address_create(self):
        with mock.patch.object(self.client.httpclient, "request") as request:
            body = dict(network_id="0", ip_version="4")
            bodyjson = self.client.serialize(body)
            request.return_value = (self.resp, "{}")
            self.client.create_ip_address(body)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(request.call_args[0][0].endswith(
                "/v2.0/ip_addresses.json"))
            self.assertEqual(request.call_args[0][1], "POST")
            self.assertEqual(request.call_args[1]["body"], bodyjson)

    def test_ip_addresses_list(self):
        with mock.patch.object(self.client.httpclient, "request") as request:
            request.return_value = (self.resp, "{}")
            self.client.list_ip_addresses()
            self.assertEqual(request.call_count, 1)
            self.assertTrue(request.call_args[0][0].endswith(
                "/v2.0/ip_addresses.json"))
            self.assertEqual(request.call_args[0][1], "GET")
            self.assertIsNone(request.call_args[1]["body"])

    def test_ip_address_show(self):
        with mock.patch.object(self.client.httpclient, "request") as request:
            request.return_value = (self.resp, "{}")
            id = "1000"
            self.client.show_ip_address(id)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(request.call_args[0][0].endswith(
                "/v2.0/ip_addresses/1000.json"))
            self.assertEqual(request.call_args[0][1], "GET")
            self.assertIsNone(request.call_args[1]["body"])

    def test_ip_address_update(self):
        with mock.patch.object(self.client.httpclient, "request") as request:
            body = dict(network_id="0", ip_version="4")
            bodyjson = self.client.serialize(body)
            request.return_value = (self.resp, "{}")
            id = "1000"
            self.client.update_ip_address(id, body)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(request.call_args[0][0].endswith(
                "/v2.0/ip_addresses/1000.json"))
            self.assertEqual(request.call_args[0][1], "PUT")
            self.assertEqual(request.call_args[1]["body"], bodyjson)

    def test_ip_address_delete(self):
        with mock.patch.object(self.client.httpclient, "request") as request:
            request.return_value = (self.resp, "{}")
            id = "1000"
            self.client.delete_ip_address(id)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(request.call_args[0][0].endswith(
                "/v2.0/ip_addresses/1000.json"))
            self.assertEqual(request.call_args[0][1], "DELETE")
            self.assertIsNone(request.call_args[1]["body"])

    def test_ip_address_ports_list(self):
        with mock.patch.object(self.client.httpclient, "request") as request:
            request.return_value = (self.resp, "{}")
            ip_address_id = "1000"
            self.client.list_ip_addresses_ports(ip_address_id)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(request.call_args[0][0].endswith(
                "/v2.0/ip_addresses/1000/ports.json"))
            self.assertEqual(request.call_args[0][1], "GET")
            self.assertIsNone(request.call_args[1]["body"])

    def test_ip_address_port_update(self):
        with mock.patch.object(self.client.httpclient, "request") as request:
            body = dict(service="none")
            bodyjson = self.client.serialize(body)
            request.return_value = (self.resp, "{}")
            ip_address_id = "1000"
            port_id = "2000"
            self.client.update_ip_addresses_port(ip_address_id, port_id, body)
            self.assertEqual(request.call_count, 1)
            self.assertTrue(request.call_args[0][0].endswith(
                "/v2.0/ip_addresses/1000/ports/2000.json"))
            self.assertEqual(request.call_args[0][1], "PUT")
            self.assertEqual(request.call_args[1]["body"], bodyjson)
