from aiohttp.web_middlewares import middleware

from .base import BaseLimiter


class SlidingLog(BaseLimiter):
    @middleware
    async def handle(self, request, handler):
        ip = request.remote
        count = self._clients.get(ip, 0)

        if not count:
            self._clients[ip] = 0

        if count < self._config.max_requests:
            self._clients[ip] += 1
            return await handler(request)
        else:
            return await self._error_handler(request)
