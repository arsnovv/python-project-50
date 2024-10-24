import yaml
import argparse
import json
from gendiff.difference_generator import generate_diff


def parse_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output'
    )
    parser.add_argument(
        'first_file',
        type=str,
        help='Path to the first file'
    )
    parser.add_argument(
        'second_file',
        type=str,
        help='Path to the second file'
    )

    args = parser.parse_args()

    if args.first_file.endswith('.json') and args.second_file.endswith('.json'):
        with open(args.first_file, 'r') as file1:
            data1 = json.load(file1)

        with open(args.second_file, 'r') as file2:
            data2 = json.load(file2)

    elif (args.first_file.endswith('.yml') or args.first_file.endswith('.yaml')
          and args.second_file.endswith('.yml')
          or args.second_file.endswith('.ymal')):
        with open(args.first_file, 'r') as file1:
            data1 = yaml.safe_load(file1)

        with open(args.second_file, 'r') as file2:
            data2 = yaml.safe_load(file2)

    diff = generate_diff(data1, data2)
    return diff
