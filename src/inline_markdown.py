from typing import List
from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text
            if text_type == TextType.ITALIC:
                node_text = node_text.replace("**", "__BOLD__")
            split_value = node_text.split(delimiter)
            if len(split_value) % 2 != 1:
                raise Exception(
                    f"Invalid Markdown: Uneven number of {delimiter} delimiters."
                )
            for i in range(len(split_value)):
                if split_value[i] != "":
                    node_type = TextType.TEXT if i % 2 == 0 else text_type
                    new_nodes.append(
                        TextNode(split_value[i].replace("__BOLD__", "**"), node_type)
                    )
    return new_nodes


def split_nodes_images(old_nodes):
    regex = r"!\[(?:[^\[\]]*)\]\((?:[^\(\)]*)\)"
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text
            images = extract_markdown_images(node_text)
            image_nodes = []
            for image in images:
                image_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            split_text = re.split(regex, node_text)
            if len(split_text) == 0:
                return image_nodes
            for i in range(len(split_text)):
                if split_text[i]:
                    new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                if i < len(image_nodes):
                    new_nodes.append(image_nodes[i])
    return new_nodes


def split_nodes_links(old_nodes):
    regex = r"(?<!!)\[(?:[^\[\]]*)\]\((?:[^\(\)]*)\)"
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_text = node.text
            links = extract_markdown_links(node_text)
            link_nodes = []
            for link in links:
                link_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            split_text = re.split(regex, node_text)
            for i in range(len(split_text)):
                if split_text[i]:
                    new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                if i < len(link_nodes):
                    new_nodes.append(link_nodes[i])
    return new_nodes


def extract_markdown_images(text: str) -> List:
    image_regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(image_regex, text)
    return matches


def extract_markdown_links(text: str):
    link_regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(link_regex, text)
    return matches


def split_markdown_nodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_links(nodes)

    return nodes
