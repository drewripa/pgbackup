import pytest

from pgbackup import cli
# pgbackup postgres://user@example.com:5432/db_one --driver s3 backups

url = "postgres://user@example.com:5432/db_one"

def test_parser_without_driver():
    """
    Without a specified driver the parser will exit
    :return:
    """
    with pytest.raises(SystemExit):
        parser = cli.create_parser()
        parser.parse_args([url])

def test_parser_with_driver():
    """
    The parser will exit if it receives a driver without a destination
    :return:
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_driver_with_unknown_driver():
    """
    The parser will exit if the driver name is unknown
    :return:
    """
    parser = cli.create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_drivers():
    """
    The parser will not exit if the driver name is known
    :return:
    """
    parser = cli.create_parser()
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])


def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it receives a driver and destination
    :return:
    """
    parser = cli.create_parser()

    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.url == url
    assert args.driver == 'local'
    assert args.destination == '/some/path'