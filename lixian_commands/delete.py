from lixian_commands.util import *
from lixian_cli_parser import *
from lixian_config import get_config
from lixian_encoding import default_encoding
from lixian_colors import colors
import lixian_help
import lixian_query


@command_line_parser(help=lixian_help.delete)
@with_parser(parse_login)
@with_parser(parse_colors)
@with_parser(parse_logging)
@command_line_option('i')
@command_line_option('all')
@command_line_option('failed')
@command_line_value('limit', default=get_config('limit'))
@command_line_value('page-size', default=get_config('page-size'))
def delete_task(args):
    client = create_client(args)
    to_delete = lixian_query.search_tasks(client, args)
    if not to_delete:
        print 'Nothing to delete'
        return
    with colors(args.colors).red.bold():
        print "Below files are going to be deleted:"
        for x in to_delete:
            print x['name'].encode(default_encoding)
    if args.i:
        yes_or_no = raw_input('Are your sure to delete them from Xunlei cloud? (y/n) ')
        while yes_or_no.lower() not in ('y', 'yes', 'n', 'no'):
            yes_or_no = raw_input('yes or no? ')
        if yes_or_no.lower() in ('y', 'yes'):
            pass
        elif yes_or_no.lower() in ('n', 'no'):
            print 'Deletion abort per user request.'
            return
    client.delete_tasks(to_delete)
