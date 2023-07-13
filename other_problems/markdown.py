# Start
# #
# ##
# *

# End \n

def convert(markdown):
    statements = markdown.split("\n")
    print(statements)
    result = []
    items = []
    start_item = False
    for i, statement in enumerate(statements):
        if start_item and statement[0] != "*":
            start_item = False
            result.extend(process_items(items))
            items = []
        elif statement[:2] == "##":
            result.append("<h2>" + statement[1:] + "</h2>")
            continue
        elif statement[0] == "#":
            result.append("<h1>" + statement[1:] + "</h1>")
        elif statement[0] == "*":
            start_item = True
            items.append(statement[1:])
            if i == len(statements) - 1:
                result.extend(process_items(items))
    return "".join(result)

def process_items(items):
    result = []
    result.append("<ul")
    for item in items:
        result.append("<li>" + item + "</li>")
    result.append("</ul>")
    return result


testcase_0 = "# This is a header \n## this is a subheader"
testcase_1 = "# This is a header\nThis is a paragraph\n* This is a list item\n* Another list item"
testcase_2 = "Some text \n the rest of it"
testcase_3 = " # some header"
testcase_4 = "* item 1 \n* item 2 \n* item 3"

print(convert(testcase_0))
print(convert(testcase_4))

