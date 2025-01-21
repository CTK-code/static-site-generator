import os
import shutil

from generate_page import generate_page, generate_page_recursive


def print_directory(path: str, level: int):
    for file in os.listdir(path):
        print(level * " " + "|_" + file)
        new_path = os.path.join(path, file)
        if os.path.isdir(new_path):
            print_directory(os.path.join(path, file), level + 1)


def copy_directory(source_dir: str, target_dir: str):
    if not os.path.exists(source_dir):
        raise ValueError(f"Soure Directory {source_dir} does not exist")
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
    os.mkdir(target_dir)
    for file in os.listdir(source_dir):
        new_path = os.path.join(source_dir, file)
        if os.path.isdir(new_path):
            new_dir = os.path.join(target_dir, file)
            copy_directory(os.path.join(source_dir, file), new_dir)
        else:
            print(f"Copying {file} from {source_dir} to {target_dir}")
            old_file = os.path.join(source_dir, file)
            new_file = os.path.join(target_dir, file)
            shutil.copy(old_file, new_file)


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    static_folder = os.path.join(dir_path, "../static")
    public_folder = os.path.join(dir_path, "../public/")
    content_path = os.path.join(dir_path, "../content/")
    template_path = os.path.join(dir_path, "../template.html")
    if os.path.exists(public_folder):
        shutil.rmtree(public_folder)
    os.mkdir(public_folder)
    copy_directory(static_folder, public_folder)
    generate_page_recursive(content_path, template_path, public_folder)


if __name__ == "__main__":
    main()
