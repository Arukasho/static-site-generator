
class HTMLNode():
    def __init__(self, tag:str=None, value:str=None, children:list=None, props:dict=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented Error")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        
        att_list = list(self.props.keys())
        attributes = ""

        for att in att_list:
            attributes += f"{att}={self.props[att]} "

        return attributes
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
