def stylish(diff, level=0):
    indent = ' ' * (level * 2)
    result = []

    grouped_diff = {}

    # Собираем изменения по ключам
    for item in diff:
        key = item['key']
        status = item['status']

        if key not in grouped_diff:
            grouped_diff[key] = {'added': [], 'removed': [], 'unchanged': []}

        # Обрабатываем изменения по статусу
        if status == 'modified':
            grouped_diff[key]['removed'].append(f" - {key}: {format_value(item['old_value'], level)}")
            grouped_diff[key]['added'].append(f" + {key}: {format_value(item['new_value'], level)}")
        elif status == 'unchanged':
            grouped_diff[key]['unchanged'].append(f" {key}: {format_value(item['value'], level)}")
        elif status == 'removed':
            grouped_diff[key]['removed'].append(f" - {key}: {format_value(item['value'], level)}")
        elif status == 'added':
            grouped_diff[key]['added'].append(f" + {key}: {format_value(item['value'], level)}")

    # Обрабатываем изменения для каждого ключа
    for key, changes in grouped_diff.items():
        if changes['removed'] or changes['added']:
            result.append(f"{indent}{key}: {{")
            if changes['removed']:
                for line in changes['removed']:
                    result.append(f"{indent}  {line}")
            if changes['added']:
                for line in changes['added']:
                    result.append(f"{indent}  {line}")
            result.append(f"{indent}}}")
        elif changes['unchanged']:
            for unchanged in changes['unchanged']:
                result.append(f"{indent}{unchanged}")

    return '\n'.join(result)


def format_value(value, level):
    indent = ' ' * ((level + 1) * 2)

    if isinstance(value, dict):
        formatted_dict = ['{']
        for k, v in value.items():
            formatted_dict.append(f"{indent}{k}: {format_value(v, level + 1)}")
        formatted_dict.append(f"{' ' * (level * 2)}}}")
        return '\n'.join(formatted_dict)
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


