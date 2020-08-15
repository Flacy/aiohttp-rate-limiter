import pytest
from aiohttp import web
from aiohttp_rate_limiter import setup as setup_rate


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    setup_rate(app, method='fixed_window', max_requests=1, interval=100)
    return loop.run_until_complete(aiohttp_client(app))


async def test_block(cli):
    resp = await cli.get('/')
    assert resp.status == 404
    resp = await cli.get('/')
    assert resp.status == 429
