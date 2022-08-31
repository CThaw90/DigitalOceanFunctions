# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main(args):
    # Use a breakpoint in the code line below to debug your script.
    name = args.get('name')
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    return {'name': name}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main({'name': 'PyCharm'})

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
