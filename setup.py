import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-gen",
    version="0.1.0",
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="A command-line tool to generate Flask projects and applications.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/htshongany/Flask-Init",
    packages=setuptools.find_packages(),
    package_dir={'flask_init.src': 'flask_init/src', 'flask_init': 'flask_init'},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "Flask",
        "Flask-SQLAlchemy",
        "Flask-Migrate",
        "python-dotenv",
    ],
    entry_points={
        'console_scripts': [
            'Flask-gen=flask_gen.main:main',
        ],
        'flask.commands': [
            'init=flask_gen.commands:init_cli',
        ],
    },
)