import argparse
from flask_init.src import app_creator
from flask_init.src import project_creator

def main():
    parser = argparse.ArgumentParser(
        description="Flask Project Generator",
        usage="init {project|app} <name> [path]"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'init' command
    parser_init = subparsers.add_parser("init", help="Initialize a project or an application")
    init_subparsers = parser_init.add_subparsers(dest="target", help="Initialization target")

    # Sub-command 'init project'
    parser_project = init_subparsers.add_parser("project", help="Initialize a complete Flask project")
    parser_project.add_argument("name", help="Project name")
    parser_project.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Destination path for the project (default: current directory)"
    )

    # Sub-command 'init app'
    parser_app = init_subparsers.add_parser("app", help="Initialize a new application (blueprint)")
    parser_app.add_argument("name", help="Application (blueprint) name")
    parser_app.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Project directory where the application will be created (default: current directory)"
    )

    args = parser.parse_args()

    # Detailed display of passed arguments (for debugging or confirmation)
    print("Received arguments:", args)

    if args.command == "init":
        if args.target == "project":
            project_creator.init_project(args.name, args.path)
        elif args.target == "app":
            app_creator.init_app(args.name, args.path)
        else:
            parser_init.print_help()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
