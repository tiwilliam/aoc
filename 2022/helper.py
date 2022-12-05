import os


def load_input(string, split="\n", strip=True):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    content = open(f"{base_dir}/{string}.input").read()
    if strip:
        content = content.strip()
    if split:
        return content.split(split)
    return content
