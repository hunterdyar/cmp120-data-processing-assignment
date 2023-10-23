# THis file is provided and SHOULD NOT be edited.

path = "births_00_08.txt"


def get_all_data_blob():
    """Returns the contents of the data file as a single large string"""
    file = open(path, "r")
    blob = file.read().strip()
    file.close()
    return blob


def get_lines():
    """Returns an array of strings, one per line."""
    file = open(path, "r")
    lines = file.readlines()
    file.close()

    # Filter out any items that don't evaluate to true (the default function when None is passed into filter). Empty strings are false, all other strings are true.
    # This filters out empty lines from the array.
    lines = list(filter(None, lines))

    return lines


if __name__ == '__main__':
    data = get_lines()
    print("There are "+str(len(data))+" lines of data. The first is: "+data[0].strip())
