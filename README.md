# Flask-Init

**Flask-Init** is a command-line tool for Flask that automates the creation of complete Flask projects and modular applications (blueprints), inspired by Django’s “startproject” and “startapp” commands. It simplifies the initial setup process by generating a pre-configured project structure with default configuration, error pages, database integration (using Flask-SQLAlchemy and Flask-Migrate), and more.

## Features

- **Project Generation:** Quickly create a new Flask project with a standard structure including core directories (e.g., templates, static, errors).
- **App (Blueprint) Generation:** Generate modular applications (blueprints) that can be easily registered into your project.
- **Django-Inspired Workflow:** Emulates the ease of Django’s project and app creation commands.
- **Preconfigured Setup:** Automatically creates essential files such as configuration files (`config.py`), extension initialization (`extensions.py`), and basic error templates.
- **Customizable:** Designed to be extended and adapted to fit your specific needs.

## Installation

Install **Flask-Init** using pip (make sure you have Python 3.7+ installed):

```bash
pip install flask-init
```

*Note: If the package name is not yet published on PyPI, you can install it locally by cloning the repository and using:*

```bash
pip install .
```

## Usage

Once installed, **Flask-Init** adds a new CLI group to your Flask commands. You can use the following commands:

### Initialize a New Project

To create a complete Flask project, run:

```bash
flask init project <project_name> [path]
```

Example:

```bash
flask init project my_flask_project .
```

This command will:
- Check if a project already exists in the specified directory.
- Create the necessary directory structure:
  - `core/` (with subfolders: `templates`, `static`, `templates/errors`)
  - `config.py`
  - `extensions.py`
  - `app.py`
  - `.env.example`
- Generate default content for each file, including settings and error pages.

### Initialize a New Application (Blueprint)

To create a new app (blueprint) inside an existing project, run:

```bash
flask init app <app_name> [path]
```

Example:

```bash
flask init app blog .
```

This command will:
- Check if an app with the given name already exists.
- Create a directory structure for the app:
  - `blog/` with subfolders: `models/`, `routes/`, and `templates/blog/`
- Generate boilerplate files (e.g., a default route in `routes/index.py` and a simple template).

## Project Structure

After running the project command, your project directory will look similar to this:

```
my_flask_project/
├── config.py
├── extensions.py
├── app.py
├── requirements.txt
├── .env.example
└── core/
    ├── __init__.py         # Imports the create_app function from settings
    ├── settings.py         # Contains the create_app function with default configuration
    ├── urls.py             # Placeholder for blueprint registration
    ├── templates/
    │   ├── base.html       # Base HTML template
    │   └── errors/
    │       ├── 404.html
    │       ├── 403.html
    │       └── 500.html
    └── static/
        └── styles.css      # Empty CSS file for customization
```

Similarly, when generating a new application, a structure like the following will be created:

```
blog/
├── models/
├── routes/
│   ├── index.py          # Contains a sample route that renders a template
│   └── urls.py           # Registers the blueprint with a URL prefix
└── templates/
    └── blog/
        └── index.html    # Sample template for the blog app
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests on the [GitHub repository](https://github.com/htshongany/Flask-Init). Please follow the guidelines in the CONTRIBUTING.md file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
