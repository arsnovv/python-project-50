import argparse
import json
from gendiff.difference_generator import generate_diff


def main():
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
        help='Path to the first JSON file'
    )
    parser.add_argument(
        'second_file',
        type=str,
        help='Path to the second JSON file'
    )

    args = parser.parse_args()

    with open(args.first_file, 'r') as file1:
        data1 = json.load(file1)

    with open(args.second_file, 'r') as file2:
        data2 = json.load(file2)

    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == '__main__':
    main()
