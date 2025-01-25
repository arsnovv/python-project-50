from gendiff.difference_generator import generate_diff
from gendiff.stylish import stylish

def test_generate_diff():
    dict1 = {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": True,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }
    dict2 = {
        "common": {
            "follow": False,
            "setting1": "Value 1",
            "setting3": None,
            "setting4": "blah blah",
            "setting5": {
                "key5": "value5"
            },
            "setting6": {
                "key": "value",
                "ops": "vops",
                "doge": {
                    "wow": "so much"
                }
            }
        },
        "group1": {
            "foo": "bar",
            "baz": "bars",
            "nest": "str"
        },
        "group3": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
    expected_output = """{
      - common:
          - follow: false
          - setting2: 200
          - setting3: true
          + setting3: null
          + setting4: blah blah
          + setting5: {
                key5: value5
            }
          + setting6: {
                key: value
                ops: vops
                doge: {
                  - wow:
                  + wow: so much
                }
            }
      - group2: {
            abc: 12345
            deep: {
                id: 45
            }
        }
      + group3: {
            deep: {
                id: {
                    number: 45
                }
            }
            fee: 100500
        }
    }
"""
    assert generate_diff(dict1, dict2, format_name='stylish') == expected_output

