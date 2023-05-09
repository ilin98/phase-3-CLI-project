#!/user/bin/env python3

from helpers import search, get_lineup

if __name__ == '__main__':
    print('Welcome to my CLI!')
    search_query = search()
    while True:

        if search_query == 'lineup':
            if not get_lineup():
                search_query = search()
        elif search_query == 'exit':
            print('Goodbye!')
            break
        else:
            print('Invalid command.')
            search_query = search()
    print('Thanks for using my CLI!')
