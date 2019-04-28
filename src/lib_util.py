import shutil

def get_terminal_size():
    return shutil.get_terminal_size((80, 20))

def print_row(item):
    print(f"{item['name']} ({item['id']})")
    print(item['answer'], '\n')

def reset_index(df):
    return df.reset_index().drop('index', axis='columns')

def split_lines(item):
    split_text = [x.replace('\xa0', '') for x in item.splitlines()]
    return list(filter(None, split_text))