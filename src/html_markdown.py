from block_markdown import block_to_block_type, markdown_to_block, BlockType
from htmlnode import LeafNode, ParentNode
from inline_markdown import split_markdown_nodes
from textnode import text_node_to_html_node


def markdown_to_html_nodes(markdown):
    blocks = markdown_to_block(markdown)
    children = []
    for block in blocks:
        if len(block) == 0:
            continue
        type = block_to_block_type(block)
        match type:
            case "code":
                children.append(markdown_to_code_node(block))
            case "ordered_list":
                children.append(markdown_to_list_nodes(block, "ol"))
            case "unordered_list":
                children.append(markdown_to_list_nodes(block, "ul"))
            case "quote":
                children.append(markdown_to_quote_node(block))
            case "heading":
                children.append(markdown_to_header_node(block))
            case _:
                children.append(markdown_to_paragraph_node(block))
    return ParentNode("div", children=children)


def text_to_children(text):
    nodes = split_markdown_nodes(text)
    children = []
    for node in nodes:
        children.append(text_node_to_html_node(node))
    return children


def markdown_to_list_nodes(block, list_tag):
    children = []
    list_items = block.split("\n")
    start = 2 if list_tag == "ul" else 3
    for item in list_items:
        children.append(ParentNode("li", text_to_children(item[start:])))

    return ParentNode(list_tag, children=children)


def markdown_to_header_node(block):
    header_size = 0
    for i in range(len(block)):
        if block[i] == "#":
            header_size = i + 1
    if header_size == 0 or header_size > 6:
        return ParentNode("p", text_to_children(block))
    return ParentNode(f"h{header_size}", text_to_children(block[header_size + 1 :]))


def markdown_to_quote_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


def markdown_to_paragraph_node(block):
    children = text_to_children(block)
    return ParentNode("p", children)


def markdown_to_code_node(block):
    return ParentNode(
        "pre", children=[ParentNode("code", text_to_children(block[3:-3]))]
    )


# Currently unneeded methods that stem from my misunderstanding of the question
def markdown_to_unordered_list(block):
    html = "<ul>"
    list_items = block.split("\n")
    for item in list_items:
        html += f"<li>{item[2:]}</li>"

    return html + "</ul>"


def markdown_to_header(block):
    header_size = 0
    for i in range(len(block)):
        if block[i] != "#":
            header_size = i + 1
    if header_size == 0 or header_size > 6:
        return f"<p>{block}</p>"
    return f"<h{header_size}>{block}</h{header_size}>"


def markdown_to_ordered_list(block):
    html = "<ol>"
    list_items = block.split("\n")
    for item in list_items:
        html += f"<li>{item[3:]}</li>"

    return html + "</ol>"


def markdown_to_paragraph(block):
    return f"<p>{block}</p>"


def markdown_to_code(block):
    return f"<pre><code>{block[3:-3]}</code></pre>"


def markdown_to_quote(block):
    html = "<blockquote>"
    quotes = block.split("\n")
    for quote in quotes:
        html += f"<p>{quote[2:]}</p>"
    return html + "</blockquote>"
