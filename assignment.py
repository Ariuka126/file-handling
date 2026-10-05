# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
    with open(filename, "w") as f:
        for i, item in enumerate(items, start=1):
            f.write(f"{i}. {item}\n")
# Exercise 2
def read_names(filename):
    names = []
    with open(filename, "r") as f:
        for line in f:
            cleaned = line.strip()
            if cleaned:
                names.append(cleaned)
    return names

# Exercise 3
def append_entry(filename, text):
    # Write your code here
    pass

# Exercise 4
def search_file(filename, word):
    # Write your code here
    pass

# Exercise 5
def number_the_lines(source, destination):
    # Write your code here
    pass
