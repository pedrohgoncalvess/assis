# Assis: Automated Documentation for Data Engineering Projects

**Assis** is a Python package designed to automate the generation of documentation for data engineering projects. It scans your project files, processes them, and creates comprehensive documentation based on your codebase using natural language processing. The tool can be particularly useful for generating README files or technical documentation for data engineering workflows, pipelines, and systems.

## Features
- **Automated documentation generation**: Scans your project directory and creates documentation files such as README.md.
- **Multi-language support**: Generates documentation in multiple languages (default is Portuguese, `pt-br`).
- **Customizable file search**: Allows the user to ignore certain directories when generating documentation.
- **API Integration**: Utilizes OpenAI API to generate meaningful documentation based on the project structure.

## Installation
To install the package, you can clone the repository and install the dependencies:

```bash
pip install assis
```

Make sure to set up your environment variables or provide an OpenAI API key when running the script.

## Usage

### Basic Command

To generate documentation for your project, simply run the following command:

```bash
assis --path /path/to/your/project --key your_openai_api_key
```

### Arguments

- `--path` (required): The path to the directory where your data engineering project resides.
- `--lang`: The language in which you want the documentation to be generated. Default is Portuguese (`pt-br`).
- `--ignore`: Directories to ignore during documentation generation. *.idea, .git, .venv, venv, \__pycache__, .history, build will always be ignored*
- `--key`: OpenAI API key for generating the documentation. If not provided, the key should be available in environment variables as `OPENAI_API_KEY`.

### Files

This will generate the following files in your project directory:
- `assis-doc.log.json`: A log of the input and output tokens used during documentation generation.
- `README.md`: The generated documentation file for your project.

## Environment Variables

If you prefer not to pass the OpenAI API key via the command line, you can create a `.env` file in your project root with the following content:

```
OPENAI_API_KEY=your_openai_api_key
```

The package will automatically load this environment variable during runtime.

## Contributing

Feel free to submit issues or pull requests if you want to contribute to improving **Assis**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.