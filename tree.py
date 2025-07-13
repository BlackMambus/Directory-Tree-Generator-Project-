import os

def generate_tree(path, prefix=""):
    """Recursively prints a directory tree structure."""
    if not os.path.isdir(path):
        print(f"{path} is not a valid directory.")
        return

    entries = sorted(os.listdir(path))
    entries_count = len(entries)

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "├── " if index < entries_count - 1 else "└── "
        print(prefix + connector + entry)

        if os.path.isdir(full_path):
            extension = "│   " if index < entries_count - 1 else "    "
            generate_tree(full_path, prefix + extension)

# Example usage
if __name__ == "__main__":
    root_dir = input("Enter the path of the directory: ").strip()
    print(f"\n📁 Directory Tree for: {root_dir}\n")
    generate_tree(root_dir)




