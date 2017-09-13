import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
supported_distros = ['debian', 'ubuntu', 'centos', 'redhat']


def test_gpg_through_key_apt_repository_file(host):
    assert host.system_info.distribution in supported_distros

    if host.system_info.distribution == 'debian':
        f = host.file('/etc/apt/sources.list.d/apt_syncthing_net.list')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert oct(f.mode) == '0644'
        assert f.contains('deb https://apt.syncthing.net/ syncthing stable')
    elif host.system_info.distribution == 'ubuntu':
        f = host.file('/etc/apt/sources.list.d/apt_syncthing_net.list')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert oct(f.mode) == '0644'
        assert f.contains('deb https://apt.syncthing.net/ syncthing stable')


def test_gpg_through_repo_apt_repository_file(host):
    assert host.system_info.distribution in supported_distros

    if host.system_info.distribution == 'debian':
        f = host.file(
            '/etc/apt/sources.list.d/repo_mongodb_org_apt_debian.list')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert oct(f.mode) == '0644'
        assert f.contains('deb http://repo.mongodb.org/apt')
    elif host.system_info.distribution == 'ubuntu':
        f = host.file(
            '/etc/apt/sources.list.d/repo_mongodb_org_apt_ubuntu.list')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert oct(f.mode) == '0644'
        assert f.contains('deb http://repo.mongodb.org/apt')


def test_gpg_through_rpm_repository(host):
    assert host.system_info.distribution in supported_distros

    if host.system_info.distribution == 'centos':
        f = host.file(
            '/etc/yum.repos.d/Mariadb.repo')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert oct(f.mode) == '0644'
        assert f.contains('https://yum.mariadb.org/10.2/CentOS7.3.1611-amd64')

    elif host.system_info.distribution == 'redhat':
        f = host.file(
            '/etc/yum.repos.d/Mariadb.repo')
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert oct(f.mode) == '0644'
        assert f.contains('https://yum.mariadb.org/10.2/RedHat7.3.1611-amd64')
