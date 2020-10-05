from aiohttp.web_middlewares import middleware

from aiohttp_rate_limiter.limiters.base import BaseLimiter


class FixedWindow(BaseLimiter):
    def _check_typing(self):
        cfg = self._config
        assert type(cfg.max_requests) == int
        assert type(cfg.interval) == int

    @middleware
    async def handle(self, request, handler):
        if self._count < self._config.max_requests:
            self._count += 1
            return await handler(request)
        else:
            return await self._error_handler(request)
