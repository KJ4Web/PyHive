def list_to_dict(pairs):
    return dict(pairs)

pairs = input("Enter a list: ").split(",")

pairs = [tuple(pair.split(":")) for pair in pairs]

result_dict = list_to_dict(pairs)
print("Converted dictionary:", result_dict)