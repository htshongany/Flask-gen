import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Flask-init",
    version="0.1.0",
    author="Tshongani Hamadou",
    author_email="sirehtshongany@gmail.com",
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
        "Flask>=2.0.0,<3.0.0",
        "Flask-SQLAlchemy>=2.5.0,<3.0.0",
        "Flask-Migrate>=3.0.0,<4.0.0",
        "python-dotenv>=0.15.0,<2.0.0",
    ],
    entry_points={
        'console_scripts': [
            'flask-init=flask_init.main:main',
        ],
        'flask.commands': [
            'init=flask_init.commands:init_cli',
        ],
    },
)