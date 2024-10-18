from gendiff.difference_generator import generate_diff


def test_generate_diff():
    dict1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": "false"
    }
    dict2 = {
        "timeout": 20,
        "verbose": "true",
        "host": "hexlet.io"
    }
    expected_output = (
        "{\n"
        "  - follow: false\n"
        "    host: hexlet.io\n"
        "  - proxy: 123.234.53.22\n"
        "  - timeout: 50\n"
        "  + timeout: 20\n"
        "  + verbose: true\n"
        "}"
    )
    assert generate_diff(dict1, dict2) == expected_output
