from process_nodes import *
import os
import shutil


def copy_directory(src_path, dst_path):
    paths = os.listdir(src_path)

    for path in paths:
        new_src = os.path.join(src_path, path)
        new_dst = os.path.join(dst_path, path)

        if os.path.isdir(new_src):
            os.makedirs(new_dst, exist_ok=True)
            copy_directory(new_src, new_dst)

        elif os.path.isfile(new_src):
            shutil.copy2(new_src, new_dst)


def extract_title(markdown):
    match = re.match(r"^\#\s(.*)", markdown)

    if match:
        return match.group(1)


def modify_template(template, title, content):
    new_template = template.replace("{{ Title }}", title)
    new_template = new_template.replace("{{ Content }}", content)

    return new_template


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as file:
        text = file.read()

    title = extract_title(text)
    content = markdown_to_htmlnode(text)

    with open(template_path, "r") as file:
        template = file.read()
        new_template = modify_template(template, title, content)

    with open(dest_path, "w") as file:
        file.write(new_template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    paths = os.listdir(dir_path_content)

    for path in paths:
        src = os.path.join(dir_path_content, path)
        dst = os.path.join(dest_dir_path, path)

        if os.path.isdir(src):
            os.makedirs(dst, exist_ok=True)
            generate_pages_recursive(src, template_path, dst)

        if os.path.isfile(src):
            modified_path = path.replace("md", "html")
            dst = os.path.join(dest_dir_path, modified_path)
            generate_page(src, template_path, dst)


def main():
    generate_pages_recursive("content", "template.html", "public")


main()
