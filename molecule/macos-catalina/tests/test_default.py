import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_java_toolchain(host):
    f = host.file("/tmp/java")
    assert f.exists

    cmd = host.run("/tmp/java/jdk5/bin/java -version")
    assert cmd.stderr == """java version \"1.5.0_22\"
Java(TM) 2 Runtime Environment, Standard Edition (build 1.5.0_22-b03)
Java HotSpot(TM) 64-Bit Server VM (build 1.5.0_22-b03, mixed mode)
"""

    cmd = host.run("/tmp/java/jdk6/bin/java -version")
    assert cmd.stderr == """java version \"1.6.0_45\"
Java(TM) SE Runtime Environment (build 1.6.0_45-b06)
Java HotSpot(TM) 64-Bit Server VM (build 20.45-b01, mixed mode)
"""

    cmd = host.run("/tmp/java/jdk7/bin/java -version")
    assert cmd.stderr == """java version \"1.7.0_79\"
Java(TM) SE Runtime Environment (build 1.7.0_79-b15)
Java HotSpot(TM) 64-Bit Server VM (build 24.79-b02, mixed mode)
"""

    cmd = host.run("/tmp/java/jdk8/bin/java -version")
    assert cmd.stderr == """java version \"1.8.0_162\"
Java(TM) SE Runtime Environment (build 1.8.0_162-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.162-b12, mixed mode)
"""

    cmd = host.run("/tmp/java/jdk9/bin/java -version")
    assert cmd.stderr == """java version \"9\"
Java(TM) SE Runtime Environment (build 9+181)
Java HotSpot(TM) 64-Bit Server VM (build 9+181, mixed mode)
"""

    cmd = host.run("/tmp/java/jdk11/bin/java -version")
    assert cmd.stderr == """java version \"11.0.1\" 2018-10-16 LTS
Java(TM) SE Runtime Environment 18.9 (build 11.0.1+13-LTS)
Java HotSpot(TM) 64-Bit Server VM 18.9 (build 11.0.1+13-LTS, mixed mode)
"""
