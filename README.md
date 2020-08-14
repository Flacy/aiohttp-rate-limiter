# aiohttp-rate-limiter

A library for control and limiting requests with aiohttp framework

### Usage
```
from aiohttp import web
from aiohttp_rate_limiter import Config, setup


app = web.Application()
cfg = Config(method='fixed_window', max_requests=100)
setup(app, config=cfg)

web.run_app(app)
```

### Requirements:
* Python >= 3.7.x
* aiohttp >= 3.5.2
