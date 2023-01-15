from aiohttp import web

from db import pg_context
from routes import setup_routes
from settings import config

app = web.Application()
setup_routes(app)
app['config'] = config
app.cleanup_ctx.append(pg_context)

web.run_app(app)