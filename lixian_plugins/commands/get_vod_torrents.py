from lixian_plugins.api import command

from lixian_cli_parser import command_line_parser
from lixian_cli_parser import with_parser
from lixian_cli import parse_login
from lixian_commands.util import create_client


@command(name='get-vod-torrents', usage='download all torrents from vod.xunlei.com')
@command_line_parser()
@with_parser(parse_login)
def get_vod_torrents(args):
    '''
    usage: lx get-vod-torrents [folder]...
    '''
    client = create_client(args)
    client.download_torrents_from_vod(0, args[0] if len(args) != 0 else '.\\vod')
