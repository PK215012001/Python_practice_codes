test = 'test string'

def find_index(source, target):
    """Function to find the index of target from the source"""
    if target not in source:
        return 'not found'
    else:
        return source.index(target)