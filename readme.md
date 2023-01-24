# psr.container

[PSR-11][psr-url] (php standard recommendation) port for python 3.5+

---

This repository holds all interfaces related to [PSR-11 (Container)][psr-url].

Note that this is not a container implementation of its own. 
It is merely interfaces that describe the components of a container.
See the specification for more details.

## Architecture overview

[![Architecture overview][architecture-overview]][architecture-overview]

## Installation

```sh
pip install psr.container --index-url=https://source.md.land/python/
```

## [Documentation](docs/index.md)

Read documentation with examples: https://development.md.land/python/psr.container/

---

Take a look for [md.di](../md.di/) — the first implementation.

[psr-url]: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-11-container.md
[architecture-overview]: docs/_static/architecture.class-diagram.svg
