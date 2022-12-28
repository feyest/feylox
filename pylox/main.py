"""Run the main pylox interpreter"""
import argparse
import runpy


def main() -> None:
    """Run the main pylox interpreter"""
    argParser = argparse.ArgumentParser(description="pylox: a python lox interpreter")
    argParser.add_argument("--filepath", "-fp", type=str, help="path to the lox file to run")

    args = argParser.parse_args()

    try:
        runpy.run_path(args.filepath)
    except FileNotFoundError:
        print(f"File not found: {args.filepath}")
    except Exception as e:
        print(f"Something went wrong running {args.filepath}")
        print(f"Error: {e}")
        exit(-1)


if __name__ == "__main__":
    """Run the main script for the python Lox interpreter"""
    main()
