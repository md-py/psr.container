# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased
### Changed

- Argument types of `ContainerInterface.get` and `ContainerInterface.has` 
  extended from `id_: str` to `id_: typing.Union[str, type]`

## [1.0.0] - 2023-01-24

- Initial commit

[1.0.0]: https://github.com/md-py/psr.container/releases/tag/1.0.0
