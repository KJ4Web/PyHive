a = "hello"
b = "b2b2b2"
c = "3g3g"
d = a + b + c

print("Uppercase:", d.upper())
print("Lowercase:", d.lower())
print("Titlecase:", d.title())
print("Stripped:", d.strip())
print("Is digit:", d.isdigit())
print('Find "3g":', d.find("3g"))
print("Capitalize:", d.capitalize())
print("Alphanumeric:", d.isalnum())
print('Count "b2":', d.count("b2"))
print("Split:", d.split())
print("Swapcase:", d.swapcase())
print("Left strip:", d.lstrip("h"))
print('Replace "hello" with "python":', d.replace("hello", "python"))