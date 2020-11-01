from aiohttp.web_middlewares import middleware

from .base import BaseLimiter


class FixedWindow(BaseLimiter):
    @middleware
    async def handle(self, request, handler):
        if self._count < self._config.max_requests:
            self._count += 1
            return await handler(request)
        else:
            return await self._error_handler(request)
