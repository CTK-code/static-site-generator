import os
from html_markdown import markdown_to_html_nodes


def extract_title(markdown):
    markdown = markdown.split("\n\n")
    if markdown[0].startswith("# "):
        return markdown[0][2:]
    raise Exception("markdown does not start with an h1")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as t:
        template = t.read()

    title = extract_title(markdown)
    node = markdown_to_html_nodes(markdown)
    content = node.to_html()
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    with open(dest_path, "w") as d:
        d.write(template)
    return template


def generate_page_recursive(dir_path_content, template_path, dir_path_dest):
    if not os.path.exists(dir_path_content):
        raise ValueError(f"Soure Directory {dir_path_content} does not exist")
    if not os.path.exists(dir_path_dest):
        os.mkdir(dir_path_dest)

    for file in os.listdir(dir_path_content):
        print(file)
        file_html = file[:-2] + "html"
        new_path = os.path.join(dir_path_dest, file)
        content_path = os.path.join(dir_path_content, file)

        if os.path.isdir(content_path):
            generate_page_recursive(content_path, template_path, new_path)
        else:
            generate_page(
                content_path, template_path, os.path.join(dir_path_dest, file_html)
            )
