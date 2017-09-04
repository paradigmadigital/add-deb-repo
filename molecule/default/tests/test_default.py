import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_gpg_through_key_apt_repository_file(host):
    f = host.file('/etc/apt/sources.list.d/apt_syncthing_net.list')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'
    assert f.contains('deb https://apt.syncthing.net/ syncthing stable')


def test_gpg_through_repo_apt_repository_file(host):
    f = host.file('/etc/apt/sources.list.d/repo_mongodb_org_apt_ubuntu.list')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0644'
    assert f.contains('deb http://repo.mongodb.org/apt')
