class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list | None = None,
        props: dict | None = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props is None:
            return ""

        # Build the string
        s = ""
        for k, v in self.props.items():
            s += f' {k}="{v}"'
        return s

    def __repr__(self):
        return (
            f"HTMLNode(tag='{self.tag}' value='{self.value}'"
            f"children='{self.children}' props='{self.props}')"
        )

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.children == other.children
            and self.value == other.value
            and self.props == other.props
        )


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict | None = None,
    ):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError(f"{self} value cannot be None")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag='{self.tag}' value='{self.value}' props='{self.props}')"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag cannot be None")
        if self.children is None or len(self.children) == 0:
            raise ValueError("children cannot be None or empty")
        output = f"<{self.tag}>"
        for child in self.children:
            output += child.to_html()
        return output + f"</{self.tag}>"

    def __repr__(self):
        return (
            f"ParentNode(tag='{self.tag}'"
            f"children='{self.children}' props='{self.props}')"
        )
