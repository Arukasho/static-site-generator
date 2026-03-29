from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag:str, children:list, props:dict=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node should have a tag")
        if self.children is None:
            raise ValueError("Parent node should have children")
        childs = ""
        if self.props is not None:
            for child in self.children:
                childs += child.to_html()

            return f'<{self.tag}{super().props_to_html()}>{childs}</{self.tag}>'

        else:
            for child in self.children:
                childs += child.to_html()

            return f'<{self.tag}>{childs}</{self.tag}>'           
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"