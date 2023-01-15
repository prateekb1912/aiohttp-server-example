from aiohttp import web
import aiohttp_jinja2
import jinja2

from db import pg_context
from routes import setup_routes
from settings import config, BASE_DIR

app = web.Application()

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(str(BASE_DIR / 'polls' / 'templates')))

setup_routes(app)
app['config'] = config
app.cleanup_ctx.append(pg_context)

web.run_app(app)