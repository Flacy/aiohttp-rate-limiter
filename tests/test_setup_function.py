import pytest
from aiohttp import web
from aiohttp_rate_limiter import setup as setup_rate, methods


@pytest.fixture
def cli(loop, aiohttp_client):
    async def handler(request):
        return web.HTTPNotFound()
    app = web.Application()
    setup_rate(app, error_handler=handler, method=methods.FIXED_WINDOW, max_requests=1, interval=100)
    return loop.run_until_complete(aiohttp_client(app))


async def test_error_handler(cli):
    resp = await cli.get('/')
    assert resp.status == 404
    resp = await cli.get('/')
    assert resp.status == 404
