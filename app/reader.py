import re


class Reader:
    def __init__(self, file_name: str = " "):
        self.file_name = file_name
        self.list_of_period = []
        self.found_server_error = []
        self.found_server_ok = []
        self.count_error = 0
        self.count_ok = 0
        self.count = 0

    def search_by_period(self, start_time: str = " ", end_time: str = " ", start_date: str = " ", end_date: str = " "):
        """
        date format must be 01/Jul/1995:13:35:01
        :param start_time:       start of time period
        :param end_time:         end of time period
        :param start_date:       start date of period
        :param end_date:         end date of period
        :return: list_of_period
        """
        time_pattern = r'\d+/\w+/\d+:\d+:\d+:\d+'
        is_period = False
        is_period_complete = False
        self.count = 0

        file = open(self.file_name, mode='rb')
        lines = file.read().splitlines()
        file.close()

        for line in lines:
            found_start_time = re.findall(time_pattern, str(line))
            self.count += 1
            if is_period_complete is True:
                break
            for i in found_start_time:
                if i >= f"{start_date}:{start_time}":
                    is_period = True
                while is_period:
                    self.list_of_period.append(line)
                    if i > f"{end_date}:{end_time}":
                        is_period = False
                        is_period_complete = True
                    else:
                        break
        print(f"\u001b[36m scanned lines {self.count}")

    def search_server_ok(self):
        self.count_ok = 0
        self.found_server_ok = []
        ok_pattern = r' 2\d{2} '
        for line in self.list_of_period:
            if re.findall(ok_pattern, str(line)):
                self.count_ok += 1
                self.found_server_ok.append(line)

    def search_server_error(self):
        self.count_error = 0
        self.found_server_error = []
        error_pattern = r' 5\d{2} '
        for line in self.list_of_period:
            if re.findall(error_pattern, str(line)):
                self.count_error += 1
                self.found_server_error.append(line)

    def print_server_error(self):
        if self.found_server_error is []:
            print(f"\u001b[32;1m Status error: [ {self.count_error} ] - X")
        else:
            print("\u001b[31;1m _________________________________________________________")
            print(f"\u001b[31;1m Status error: {len(self.found_server_error)} - X")
            print(f"\u001b[31;1m Count error: [ {self.count_error} ] - X")
            print("\u001b[31;1m _________________________________________________________")
            print("\u001b[30;1m |server|Date|req|CODE\n")
            self.found_server_error = sorted(self.found_server_error, reverse=False,
                                             key=lambda x: str(re.findall(r' 5\d{2} ', str(x))))
            for i in self.found_server_error:
                print('\u001b[33;1m', i)

    def print_server_ok(self):
        if self.found_server_ok is []:
            print(f"\u001b[32;1m Status error: [ {self.count_ok} ] - OK")
        else:
            print("\u001b[32;1m _________________________________________________________")
            print(f"\u001b[32;1m Status OK: {len(self.found_server_ok)}")
            print(f"\u001b[32;1m Count OK: [ {self.count_ok} ] - OK")
            print("\u001b[32;1m _________________________________________________________")
            print("\u001b[30;1m |server|Date|req|CODE\n")
            for i in self.found_server_ok:
                print('\u001b[34;1m', i)
