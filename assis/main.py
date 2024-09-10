import argparse
import os
from itertools import chain

from dotenv import load_dotenv

from assis.files_man import list_files
from assis.local_openia.main import generate_doc
from assis.local_openia.utils import openai_statements, generate_statements


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate documentation for data engineering projects.")
    parser.add_argument('--path', type=str, required=True,
                        help='Path to the directory from which to generate the documentation.')
    parser.add_argument('--lang', type=str, default='pt-br',
                        help='Language for generating documentation.')
    parser.add_argument("--ignore", type=str, help="Directories to ignore.")
    parser.add_argument("--key", type=str, help="Open IA API Key.")

    args = parser.parse_args()

    project_name = os.path.basename(os.path.abspath(args.path))

    print(f"✍️ Generating documentation for the {project_name} project...")

    ignore_dirs = ['.idea', '.git', '.venv', '__pycache__', '.history', 'build', 'venv']

    if args.ignore:
        ignore_dirs.append(args.ignore)

    if not args.key:
        load_dotenv(args.path)

        if not os.getenv('OPENAI_API_KEY', None):
            load_dotenv()
        if not os.getenv('OPENAI_API_KEY', None):
            raise Exception("🔑 Enter the Open AI key with the --key parameter or in the environment variables with the value OPENAI_API_KEY")
    else:
        os.environ['OPENAI_API_KEY'] = args.key

    print("🔎 Searching for useful files and directories...")
    content = list_files(args.path, ignore_dirs)
    new_statements = []

    for name, items in content.items():
        new_statements.append(generate_statements(name, items))

    print("⚙️ Mounting the support prompt...")
    statement = openai_statements('project').format(
        language=args.lang,
        project_name=project_name,
        project_details='. '.join(list(chain.from_iterable(new_statements)))
    )

    doc_content = generate_doc(statement)

    print("✍️ Creating the log file...")
    with open(f"{args.path}/assis-doc.log.json", 'w', encoding='utf-8') as log:
        log.write(
            """
            {{
            tokens_input: {_input},
            tokens_completion: {_output},
            input_message: '{statement}',
            output_message: '{doc}'
            }}
            """.format(
                _input=doc_content.get('input_token'),
                _output=doc_content.get('output_token'),
                statement=statement,
                doc=doc_content.get('doc')
            )
        )

    print("✍️ Creating the readme...")
    with open(f"{args.path}/README.md", 'w', encoding='utf-8') as readme_file:
        readme_file.write(doc_content.get('doc'))

    print("✅ Documentation created!")
