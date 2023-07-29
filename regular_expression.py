import re

content = "<p>start.</p> <h2>This is a heading in a 123 div element</h2> <p>This is some text in a div element.</p> "
#pattern = re.compile("<h2>.*</h2>")
#pattern = re.compile("<p>([^(<p>)]*)</p>")
pattern = re.compile("(.*)shi, (.*)qu, (.*)jiedao")
#pattern = re.compile("[0-9]+")
#results = pattern.findall(content)
results = pattern.findall("beijing shi, fengtai qu, zhengyang jiedao")
print(results)