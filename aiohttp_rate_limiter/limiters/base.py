from abc import ABC, abstractmethod
from asyncio import sleep, get_event_loop
from typing import Callable

from aiohttp_rate_limiter import Config


class BaseLimiter(ABC):
    def __init__(self, config: Config, error_handler: Callable):
        self._config: Config = config

        self._count = 0
        self._clients = {}

        self._error_handler: Callable = error_handler

        self._check_typing()
        self._set_interval()

    @abstractmethod
    def handle(self):
        pass

    @abstractmethod
    def _check_typing(self):
        pass

    def _set_interval(self):
        async def clear_count(self):
            while True:
                self._count = 0
                await sleep(self._config.interval)

        loop = get_event_loop()
        loop.create_task(clear_count(self))
