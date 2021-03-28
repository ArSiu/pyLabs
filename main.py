from reader import Reader


def main():
    a = Reader("test.txt")
    # a.search_by_period("13:35:00", "13:38:00", "01/Jul/1995", "01/Jul/1998")
    a.search_by_period("13:34:59", "13:35:02", "01/Jul/1995", "01/Jul/1998")
    a.search_server_error()
    a.print_server_error()


if __name__ == '__main__':
    main()
