-----

<div align="center">

[![Poetry](https://img.shields.io/badge/packaging-poetry-cyan.svg)](https://python-poetry.org/)
[![GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

</div>

<hr>

# TOBB ETU CS Community Website

It is the website of our CS Community

[WebApp Link](https://tobb-cs-community.streamlit.app)

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before setting up the project, ensure that you have the following prerequisites installed on your machine:

- Python (version 3.9):
  (https://www.python.org/downloads/)
- Poetry (version 1.4.0):
  (https://python-poetry.org/docs/#installation)

## Installation

1. Clone the project repository:

```
git clone https://github.com/TOBB-ETU-CS-Community/Community_Website.git
```

2. Navigate to the project directory:

```
cd community_website
```

3. Install project dependencies using Poetry:

```
poetry install
```

This command will create a virtual environment and install all the necessary dependencies specified in the `pyproject.toml` file.

## Usage

1. Activate the virtual environment created by Poetry:

```
poetry shell
```

2. Run the project:

```
streamlit run "community_website/Welcome.py"
```

or click start.bat file in Windows


## Contributing

If you would like to contribute to this project, follow the guidelines below:

1. Fork the repository and clone it locally.

2. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature/your-feature
   ```

3. Make your changes and commit them with descriptive commit messages.

4. Push your changes to your forked repository:
   ```
   git push origin feature/your-feature
   ```

5. Open a pull request in the original repository, describing your changes in detail.


## License

GPL v3

---
