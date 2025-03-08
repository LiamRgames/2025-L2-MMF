#Write to file practice
file_name = "experiment"
write_to = "{}.txt".format(file_name)

text_file = open(write_to,"w+")

heading = "=== TEST HEADING ===\n"
content = "blah blah blah"
other_content = "more blah blah blah"

to_write = [heading,content,other_content]

for i in to_write:
    print(i)

for i in to_write:
    text_file.write(i)
    text_file.write("\n")