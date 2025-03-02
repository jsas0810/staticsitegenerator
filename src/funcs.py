from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        # Only process TEXT type nodes
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        # Get the text content to process
        text = old_node.text
        
        # Look for the first occurrence of the delimiter
        start_index = text.find(delimiter)
        if start_index == -1:
            # No delimiter found, keep node as is
            new_nodes.append(old_node)
            continue
            
        # Look for the closing delimiter after the first one
        end_index = text.find(delimiter, start_index + len(delimiter))
        if end_index == -1:
            # No closing delimiter - invalid markdown
            raise ValueError(f"No closing delimiter '{delimiter}' found")
        
        start_text = text[0:start_index]
        # Have to use len to find the length of delimiter and exclude it from the extracted text
        delimiter_text = text[start_index + len(delimiter):end_index]
        # Ensures we skip including the closing delimiter
        end_text = text[end_index + len(delimiter):]

        # Node text_type for start and end text will be TextType.TEXT, node for delimiter will match delimiter text_type as passed in function call
        if start_text:
            new_nodes.append(TextNode(start_text, TextType.TEXT))
        if delimiter_text:
            new_nodes.append(TextNode(delimiter_text, text_type))
        # Recursively process the remaining text
        if end_text:
            # Create a temporary node with the remaining text
            remaining_node = TextNode(end_text, TextType.TEXT)
            # Recursively call our function with this node
            result_nodes = split_nodes_delimiter([remaining_node], delimiter, text_type)
            # Add the processed nodes to our result
            new_nodes.extend(result_nodes)