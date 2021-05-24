"""
Write a Python-script that:
1. Searches for files by a given pattern (pattern can include: *, ?)
2. Displays the search result
3. Gets access rights for each file that is found and displays the result

The script should have 2 obligatory functions:
- finder - a generator function searches for files by a given pattern
 in a given path returns an absolute path of a found file.
- display_result - displays founded files and files' permission
by a given list of absolute paths (You can find an example below).

Example call:
python task_3_ex_3.py /usr/bin -p '?ython*'

Example result:
...
/usr/bin/python3.6m -rwxr-xr-x
/usr/bin/python3.7m -rwxr-xr-x
Found 12 file(s).

Note: use of glob module is prohibited.

Hint: use os.walk, stat, fnmatch
"""
import argparse
import os
import fnmatch
import stat

parser = argparse.ArgumentParser()
parser.add_argument('path', type=str)
parser.add_argument('-p', type=str)


def finder(path, pattern):
    """Searches for files by a given pattern.

    :param path: Absolute path for searching.
    :param pattern: Can consist *, ?.
    :return: absolute path of found file.
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, pattern): #.strip("'")):
                yield os.path.abspath(os.path.join(root, file))


def display_result(file_paths):
    """Displays founded file paths and file's permissions."""
    # Your code
    #print('...')
    n=0
    for file in file_paths:
        n+=1
        mode=os.stat(file).st_mode
        print(file, stat.filemode(mode))
    print("Found {} file(s).".format(n))


def main():
    args = parser.parse_args()
    display_result(finder(args.path, args.p))


if __name__ == '__main__':
    main()