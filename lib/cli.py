#!/user/bin/env python3

from helpers import search, get_lineup, get_all_position, get_standings, add_win, add_loss

if __name__ == '__main__':
    print('Welcome to my CLI!')
    search_query = search()
    while True:

        if search_query == 'lineup':
            if not get_lineup():
                search_query = search()
        elif search_query == 'position':
            if not get_all_position():
                search_query = search()
        elif search_query == 'standings':
            get_standings()
            search_query = search()
        elif search_query == 'win':
            if not add_win():
                search_query = search()
        elif search_query == 'loss':
            if not add_loss():
                search_query = search()
        elif search_query == 'quit':
            print('Goodbye!')
            break
        else:
            print('Invalid command.')
            search_query = search()
    print('Thanks for using my CLI!')
