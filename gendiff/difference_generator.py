from gendiff.stylish import stylish


def generate_diff(dict1, dict2, format_name='stylish'):
    def compare_values(value1, value2):
        if isinstance(value1, dict) and isinstance(value2, dict):
            return generate_diff(value1, value2, format_name)
        return value1 != value2

    all_keys = set(dict1.keys()).union(set(dict2.keys()))
    sorted_keys = sorted(all_keys)

    diff = []

    for key in sorted_keys:
        key1 = key in dict1
        key2 = key in dict2

        if key1 and key2:
            if compare_values(dict1[key], dict2[key]):
                diff.append({
                    "key": key,
                    "status": "modified",
                    "old_value": dict1[key],
                    "new_value": dict2[key]
                })
            else:
                diff.append({
                    "key": key,
                    "status": "unchanged",
                    "value": dict1[key]
                })
        elif key1:
            diff.append({
                "key": key,
                "status": "removed",
                "value": dict1[key]
            })
        elif key2:
            diff.append({
                "key": key,
                "status": "added",
                "value": dict2[key]
            })

    if format_name == 'stylish':
        return stylish(diff)
    return diff
