def print_leaves_on_tree(data):
    for key, value in data.items():
        if isinstance(value, dict):
            print_leaves_on_tree(value)
        elif isinstance(value, int):
            print(f"{key}:{value}")



data = {'a': 4, "bax": {'cddd': {'ddd':3}}, 'd': 5}
print_leaves_on_tree(data)