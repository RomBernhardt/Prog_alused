from typing import Optional

class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount

    def __repr__(self):
        """
        Client representation.

        :return: client's name
        """
        return self.name

    def earnings_per_day(self) -> float:
        """
        Clients earnings per day since the start.

        :return: earnings per day (float value)
        """
        if self.account_age > 0:
            return (self.current_amount - self.starting_amount) / self.account_age
        return 0.0

    def loss_per_day(self) -> float:
        """
        Clients loss per day.

        :return: loss per day (float value)
        """
        if self.account_age > 0:
            return (self.starting_amount - self.current_amount) / self.account_age
        return 0.0

def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    clients = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 5:
                    name = data[0].strip()
                    bank = data[1].strip()
                    account_age = int(data[2].strip())
                    starting_amount = int(data[3].strip())
                    current_amount = int(data[4].strip())
                    client = Client(name, bank, account_age, starting_amount, current_amount)
                    clients.append(client)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    return clients


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    clients = read_from_file_into_list(filename)
    filtered_clients = [client for client in clients if client.bank == bank]
    return filtered_clients

def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to what they started with), then return None.

    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    clients = read_from_file_into_list(filename)
    max_earnings = 0
    best_client = None

    for client in clients:
        earnings = client.earnings_per_day()

        if earnings > max_earnings:
            max_earnings = earnings
            best_client = client
        elif earnings == max_earnings and best_client is not None:
            if client.account_age < best_client.account_age:
                best_client = client

    return best_client if max_earnings > 0 else None


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.

    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    clients = read_from_file_into_list(filename)
    max_loss = 0
    worst_client = None

    for client in clients:
        loss = client.loss_per_day()

        if loss > max_loss:
            max_loss = loss
            worst_client = client
        elif loss == max_loss and worst_client is not None:
            if client.account_age < worst_client.account_age:
                worst_client = client

    return worst_client if max_loss > 0 else None
