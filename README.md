Ansible role for node-exporter
==================================

Installs node exporter on a variety of systems. By default, it will download the tar balls from the official `node_exporter` repo at <https://github.com/prometheus/node_exporter>

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-node-exporter/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `node_exporter_final_dest` | Directory where `node_exporter` should be installed | string | `/usr/local/bin` | `true |
| `node_exporter_url` | URL to download node_exporter from. This can be overwritten | string | `https://github.com/prometheus/node_exporter/releases/download/v{{ node_exporter_version }}/node_exporter-{{ nod  e_exporter_version }}.{{ distro }}-{{ architecture }}.tar.gz` | `true` |
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

Important Notes
---------------

The macos-1014 distro, and Macs in general, have the BSD version of tar installed.

Unfortunately, the [unarchive ansible module](https://docs.ansible.com/ansible/latest/modules/unarchive_module.html) is not compatible with the BSD version of tar.

The GNU version of tar can be installed via `brew install gnu-tar`, which then installs the executable at `/usr/local/bin/tar`.

In order to get ansible to use this executable, you have to specify `/usr/local/bin` first in the $PATH before `/usr/bin`.

License
-------

[Apache License](LICENSE)
