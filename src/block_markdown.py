from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_block(markdown: str):
    return markdown.split("\n\n")


def block_to_block_type(block):
    if len(block) == 0:
        raise ValueError("block cannot be length 0")
    if block[0:3] == "```" and block[-3:] == "```":
        return BlockType.CODE.value

    if "# " in block[0:7]:
        return BlockType.HEADING.value

    if block.startswith("* ") or block.startswith("- "):
        items = block.split("\n")
        for item in items:
            if item[0] != "*" and item[0] != "-":
                return BlockType.PARAGRAPH.value
        return BlockType.UNORDERED_LIST.value

    if block[0] == ">":
        items = block.split("\n")
        for item in items:
            if item[0] != ">":
                return BlockType.PARAGRAPH.value
        return BlockType.QUOTE.value

    if block[0:2] == "1.":
        items = block.split("\n")
        for i in range(len(items)):
            if items[i][0:2] != f"{i + 1}.":
                return BlockType.PARAGRAPH.value
        return BlockType.ORDERED_LIST.value

    return BlockType.PARAGRAPH.value
