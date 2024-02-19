
```markdown
# Requirements

This repository contains a `requirements.txt` file that lists the Python libraries and their versions required to run the project.

## Purpose

The `requirements.txt` file serves as a reference for the specific versions of the Python libraries used in this project. It ensures consistency among different environments and allows for easy installation of dependencies.

## How to Use

To install the required dependencies, follow these steps:

1. Ensure that Python and pip are installed on your machine.

2. Open a terminal or command prompt in the project directory.

3. Run the following command to install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This command will read the `requirements.txt` file and install the specified versions of the libraries.

## Contents

The `requirements.txt` file includes the following dependencies and more:

- `google-cloud-storage==1.45.0`
- `google-cloud-bigquery==2.28.0`
- `pandas==1.3.3`
- `python-dotenv==0.19.1`
- `APScheduler==3.8.1`

Note: Make sure to use a virtual environment or an isolated environment to avoid conflicts with other projects.

## Updating Dependencies

To update the dependencies to their latest versions, you can modify the `requirements.txt` file with the desired versions or use the following command:

```bash
pip freeze > requirements.txt
```

This command will overwrite the existing `requirements.txt` file with the latest versions of the installed packages.

```
