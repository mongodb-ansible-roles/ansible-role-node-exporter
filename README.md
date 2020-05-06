Ansible role for node-exporter
==================================

Installs node exporter on a variety of systems. By default, it will download the tar balls from the official `node_exporter` repo at <https://github.com/prometheus/node_exporter>

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `node_exporter_final_dest` | Directory where `node_exporter` should be installed | string | `/usr/local/bin` | true |
| `node_exporter_sysconfig_file_dest` | Where to put `node_exporter` config flags | string | `/etc/sysconfig/node_exporter` | false | 
| `node_exporter_systemd_description` | Description of systemd service | string | Node Exporter | false |
| `node_exporter_systemd_name` | Name of the systemd service | string | `node_exporter` | false |
| `node_exporter_systemd_service_file_dest` | Location to place systemd file | string | `/etc/systemd/system` | false |
| `node_exporter_systemd_start_cmd` | Command to execute to start `node_exporter` | string | `/usr/local/bin/node_exporter $OPTIONS` | false |
| `node_exporter_systemd_user` | User who will run the systemd service | string | `root` | false |
| `node_exporter_url` | URL to download `node_exporter` from. This can be overwritten | string | `https://github.com/prometheus/node_exporter/releases/download/v{{ node_exporter_version }}/node_exporter-{{ nod  e_exporter_version }}.{{ distro }}-{{ architecture }}.tar.gz` | true |
| `node_exporter_version` | Version of `node_exporter` to install | string | `1.0.0-rc.0` | true |

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-node-exporter
      vars:
        node_exporter_version: 1.0.0-rc.0
```

SSH Config
----------

In order to get the delegated driver to work in molecule, you must set the `SSH_CONFIG` secret in GitHub Actions.
An example would look like:
```
Host my-host-dev
  HostName my-host-dev.something.somewhere.cc
  Port 22
  IdentityFile ~/.ssh/id_rsa
  PreferredAuthentications publickey
  User cloud-user
```
The host will correspond to the list of `platforms` in the `molecule.yml` file
```
# molecule.yml
...
platforms:
  - name: my-host-dev
...
```

MacOS Specific Notes
--------------------

The macos-1014 distro, and Macs in general, have the BSD version of tar installed.

Unfortunately, the [unarchive ansible module](https://docs.ansible.com/ansible/latest/modules/unarchive_module.html) is not compatible with the BSD version of tar.

The GNU version of tar can be installed via `brew install gnu-tar`, which then installs the executable at `/usr/local/bin/tar`.

In order to get ansible to use this executable, you have to specify `/usr/local/bin` first in the $PATH before `/usr/bin`.

License
-------

[Apache License](LICENSE)
