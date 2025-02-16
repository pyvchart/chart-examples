import os

def remove_html_files(directory: str):
    for filename in os.listdir(path=directory):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            os.remove(path=file_path)
            print(f"Removed {file_path}")


if __name__ == '__main__':
    examples_dir = "examples"

    # Remove all HTML files in the examples directory
    remove_html_files(directory=examples_dir)
