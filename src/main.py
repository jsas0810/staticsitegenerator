from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    object = HTMLNode("p", "Charlie Travers will always be famous", None, {"href": "https://www.google.com"})
    print(object)

main()