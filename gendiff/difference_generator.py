def generate_diff(dict1, dict2):
    all_keys = set(dict1.keys()).union(set(dict2.keys()))
    sorted_keys = sorted(all_keys)

    output = ["{"]

    for key in sorted_keys:
        key1 = key in dict1
        key2 = key in dict2

        if key1 and key2:
            if dict1[key] == dict2[key]:
                output.append(f"    {key}: {format_value(dict1[key])}")
            else:
                output.append(f"  - {key}: {format_value(dict1[key])}")
                output.append(f"  + {key}: {format_value(dict2[key])}")
        elif key1:
            output.append(f"  - {key}: {format_value(dict1[key])}")
        elif key2:
            output.append(f"  + {key}: {format_value(dict2[key])}")

    output.append("}")

    return "\n".join(output)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value