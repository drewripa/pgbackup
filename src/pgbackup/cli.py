from argparse import Action, ArgumentParser

known_drivers = ['s3', 'local']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 's3' or'local'")
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help="URL of the PostgreSQL db for backup")
    parser.add_argument('--driver',
                        help="how and where to store the backup",
                        nargs=2,
                        action=DriverAction,
                        required=True)
    return parser
