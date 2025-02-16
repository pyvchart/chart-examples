import os
import subprocess


def run_python_scripts(directory: str):
    for filename in os.listdir(path=directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            print(f"Running {file_path}...")
            subprocess.run(["python", filename], cwd=directory)


if __name__ == "__main__":
    examples_dir = "examples"

    # Run all Python scripts in the examples directory
    run_python_scripts(examples_dir)
