# add-deb-repo

Add deb repository. The gpg key can be added through `repository_url` or through
`key_url`

## Requirements

None

## Role Variables

* `deb_repository`: Dictionary with repository information
  * `url`: Url of the repository
  * `options`: Options to the repository, such as `jessie main contrib non-free`
    or `xenial-security universe`
* `gpg_key`: Dictionary with gpg key information of the repository
  * `repository_url`: Url to the key repository
  * `key_url`: Url to the key
  * `id`: ID of the key

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
