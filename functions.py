#functions
def get_todos(filepath):
    with open (filepath, 'r') as file:
        to_dos_local = file.readlines()
    return (to_dos_local)

def write_todos(filepath,written_item):
    with open(filepath, 'w') as file:
        writtenlist_local = file.writelines(written_item)
    return (writtenlist_local)