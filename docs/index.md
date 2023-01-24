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

## Usage

If you need a container, you can use the interface like this:

```python3
import psr.container
import typing


class Client:
    def get_id(self) -> str: ...
    def get_email(self) -> str: ...

    
class ClientRepository:
    def get(self, id_: str) -> Client: ...


class RenderEmailInterface:
    def for_(self, address_list: typing.List[str]) -> str:
        raise NotImplementedError


class SendEmailInterface:
    def to(self, address_list: typing.List[str], content: str, type_: str ='text/plain') -> None:
        raise NotImplementedError


class SendLetter:  
    def __init__(
        self,
        client_repository: ClientRepository,
        render_email: RenderEmailInterface, 
        send_email: SendEmailInterface
    ) -> None:
        self._client_repository = client_repository
        self._render_email = render_email
        self._send_email = send_email
        
    def for_client(self, id_: str) -> None:
        client = self._client_repository.get(id_=id_)
        address_list = [client.get_email()]
        content = self._render_email.for_(address_list=address_list)
        self._send_email.to(address_list=address_list, content=content)


if __name__ == '__main__':
    container = ...
    assert isinstance(container, psr.container.ContainerInterface)
    
    send_weekly_digest_newsletter = container.get(id_='SendLetter.weekly_digest_newsletter')
    assert isinstance(send_weekly_digest_newsletter, SendLetter)
    
    send_weekly_digest_newsletter.for_client(id_='42')
```

You can then pick one of the implementations of the interface to get a container.

If you want to implement the interface, you can require this package and
implement `psr.log.ContainerInterface` in your code. Please read the
[specification text][psr-url] for details.

---

Take a look for [md.di](../md.di/) — the first implementation.

[psr-url]: https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-11-container.md
[architecture-overview]: _static/architecture.class-diagram.svg
