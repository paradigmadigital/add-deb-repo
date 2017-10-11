# add-repo

Add repository. The gpg key can be added through `repository_url` or through
`key_url`

## Requirements

Have `apt-transport-https` installed

## Role Variables

* `repository`: Dictionary with repository information
  * `url`: Url of the repository
  * `options`: Options to the repository, such as `jessie main contrib non-free`
    or `xenial-security universe` [Deb only]
  * `name`: Repository name [RPM only]
  * `description`: Repository description [RPM only]
* `gpg_key`: Dictionary with gpg key information of the repository
  * `repository_url`: Url to the key repository
  * `key_url`: Url to the key
  * `id`: ID of the key [Deb only]
  * `gpgcheck`: Check the repository signature [RPM only]

## Dependencies

None

## Example playbook

```yaml
- hosts: all
  roles:
    - add-deb-repo
```

## Testing

You should have [molecule](https://github.com/metacloud/molecule) installed,
then
```bash
molecule test --all
```


## License

GPLv2

## Author Information
jamatute (jamatute@paradigmadigital.com)
