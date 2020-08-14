from typing import Dict, Any, Callable

from aiohttp.web import Application, HTTPTooManyRequests

from .cfg import Config

from .limiters import FixedWindow

LIMITERS = {
    'fixed_window': FixedWindow
}


async def default_error(request):
    return HTTPTooManyRequests()


def setup(app: Application, error_handler: Callable=default_error,
            config: Config=None, **kwargs: Dict[str, Any]) -> None:
    if type(config) == Config:
        method = config.__dict__.get('method')
    elif config is not None:
        raise TypeError('Config must be a Config object')
    else:
        method = kwargs.get('method')
        config = Config(**kwargs)

    if type(method) == str:
        limiter = LIMITERS.get(method)

        if limiter:
            limiter = limiter(config, error_handler)
            app.middlewares.insert(0, limiter.handle)
        else:
            raise KeyError(f'Method "{method}" is not supported')
    elif method is not None:
        raise TypeError('The main argument "method" must be a string')
    else:
        raise KeyError('The main argument "method" is missing')