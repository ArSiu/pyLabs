from reader import Reader
import time


def main():
    start_time = time.time()

    a = Reader("test/test1.txt")

    search_period_time = time.time()
    a.search_by_period("00:00:01", "13:32:25", "01/Jul/1995", "28/Jul/1995")
    search_period_time_end = time.time()

    search_pattern_time = time.time()
    a.search_server_error()
    a.search_server_ok()
    search_pattern_time_end = time.time()

    end_time = time.time()
    print("--- %.2f seconds ---%.2f seconds---%.2f seconds" % ((end_time - start_time),
                                                               (search_period_time - search_period_time_end),
                                                               (search_pattern_time - search_pattern_time_end)))
    print(f"Errors:{a.count_error}")
    print(f"OK`s:{a.count_ok}")
    a.print_server_error()


if __name__ == '__main__':
    main()
