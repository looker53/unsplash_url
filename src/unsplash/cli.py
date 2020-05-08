"""命令行。"""
import click
from . import web
@click.argument('port')
def cli(port=5000):
    """命令行启动 flask 服务器"""
    web.app.run(port=port)

if __name__ == '__main__':
    cli()