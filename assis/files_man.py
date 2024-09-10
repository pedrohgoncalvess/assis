import os


def list_files(path:str, ignore_dirs:list[str]):
    results = {}

    for root, dirs, files in os.walk(path):
        dir_name = os.path.basename(root)

        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        if dir_name not in results:
            results[dir_name] = {}

        python_files = []
        dir_files = []

        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith('.py'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                python_files.append((file, content))
            else:
                dir_files.append(file)

        if python_files:
            results[dir_name]['python_files'] = python_files
        if dir_files:
            results[dir_name]['files'] = dir_files

    return results