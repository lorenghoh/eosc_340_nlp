import shutil

def get_terminal_size():
    return shutil.get_terminal_size((80, 20))

def print_row(item):
    print(f"{item['name']} ({item['id']})")
    print(item['answer'], '\n')
