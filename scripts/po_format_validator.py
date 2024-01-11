import os

import polib


def check_po_headers(pofile):
    headers_to_remove = ['Last-Translator', 'PO-Revision-Date', 'POT-Creation-Date', 'X-Generator', 'X-Poedit-Basepath']
    po = polib.pofile(pofile)

    existing_headers = []
    for header in headers_to_remove:
        if header in po.metadata:
            existing_headers.append(header)

    return existing_headers


print('Po file is correct. None of the unwanted headers are present.')


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pofile = os.path.join(base_dir, '.\\po\\ja_JP.po')

    # Using the function
    existing_headers = check_po_headers(pofile)

    # If specified headers exist, print them and exit with code 1
    if existing_headers:
        print(f'These headers should not exist in the po file: {", ".join(existing_headers)}')
        exit(1)


if __name__ == "__main__":
    main()
