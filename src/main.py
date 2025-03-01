from textnode import TextType, TextNode

def main():
    object = TextNode("This is a text node", TextType.BOLD_TEXT, "https://www.boot.dev")
    print(object)

main()