import os


def load_input(string):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return open(f"{base_dir}/{string}.input").read().strip()
