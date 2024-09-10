import yaml

from assis.utils import project_root


def openai_statements(part_message:str) -> dict[str:any] | None:
    with open(f'{project_root}/assis/local_openia/statement/main.yaml', encoding='utf-8') as file:
        return yaml.safe_load(file).get(part_message)


def generate_statements(name:str, items:dict, statements:list | None = None) -> list[str]:
    if statements:
        new_statements = statements
    else:
        new_statements = []

    if not items:
        new_statements.append(f"There's a directory called {name} that's empty.")
        return new_statements

    if items.get('files'):
        new_statements.append(f"The {name} directory has the following files {', '.join(items.get('files'))}.")
    elif items.get('python_files'):
        for python_file, file_content in items.get('python_files'):
            new_statements.append(
                f"The {name} directory has the python file named {python_file} {f'which has the script {file_content}' if file_content else 'which is empty.'}"
            )
    elif items.keys():
        for dir_name, dir_items in items.items():
            if dir_name not in ['files','python_files']:
                new_statements.append(generate_statements(dir_name, dir_items, new_statements))

    return new_statements