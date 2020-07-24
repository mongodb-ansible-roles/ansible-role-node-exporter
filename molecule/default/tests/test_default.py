import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_node_exporter(host):
    assert host.file("/usr/local/bin/node_exporter").exists
    cmd = host.run("/usr/local/bin/node_exporter --version 2>&1 |"
                   "sed -n 1p | awk '{print $3}'")
    assert cmd.stdout == "1.0.0-rc.0\n"
    cmd = host.run("curl localhost:9100/metrics | "
                   "grep node_exporter_build_info")
    assert cmd.succeeded
