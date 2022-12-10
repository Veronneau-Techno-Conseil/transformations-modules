
from getopt import GetoptError, getopt
import json
import sys
from configure import configure

from models import Configuration


def main(argv):
    action = ''
    config = ''
    data = ''
    
    try:
        opts, args = getopt(argv, "ha:c:d:", ["action=", "config=", "data="])
    except GetoptError:
        print("app.py -a<configure/transform> -c<configuration.json> [-d<data.json>]")
        print("app.py --action=<configure/transform> --config=<configuration.json> [--data=<data.json>]")
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("app.py -a<configure/transform> -c<configuration.json> [-d<data.json>]")
            print("app.py --action=<configure/transform> --config=<configuration.json> [--data=<data.json>]")
            sys.exit()
        elif opt in ("-a", "--action"):
            action = arg
        elif opt in ("-c", "--config"):
            config = arg
        elif opt in ("-d", "--data"):
            data = arg

    if config is None:
        raise Exception("Config is mandatory")
    
    with open(config) as f:
        config_dict = json.load(f)

    if len(config_dict) is not None:
        config_value = Configuration.from_json(config_dict)

    if action == "configure":
        configure(config_value)
    # Add transform
    #elif action == "transform":
    #    down(credentials, airbyte_url, file)


if __name__ == '__main__':
    # sys.argv[] #pass arguments if given and whatnot
    main(sys.argv[1:])
