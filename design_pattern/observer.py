import abc


class Publisher:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            raise Exception("Failed to add: {}".format(observer))

    def unregister(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print("Failed to remove: {}".format(observer))

    def notify(self, arg):
        """
        :param arg: new value to notify all the observers
        :return:
        """
        for observer in self.observers:
            observer.update(arg)


class Host(Publisher):
    """
    ConcretePublisher
    """
    def __init__(self, name):
        super(Host, self).__init__()
        self._current_highest_bid_holder = name
        self._highest_bid = 0

    @property
    def current_highest_bid_holder(self):
        return self._current_highest_bid_holder

    @current_highest_bid_holder.setter
    def current_highest_bid_holder(self, value):
        self._current_highest_bid_holder = value

    @property
    def highest_bid(self):
        return self._highest_bid

    @highest_bid.setter
    def highest_bid(self, value):
        self._highest_bid = value

    def __str__(self):
        return "Current highest bid is: {}, held by: {}".format(self.highest_bid, self.current_highest_bid_holder)


class Observer(metaclass=abc.ABCMeta):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    @abc.abstractmethod
    def update(self, arg):
        pass


class Bidder(Observer):
    def __init__(self, name, host):
        super(Bidder, self).__init__(host)
        self.name = name
        self._current_bid = 0
        self._current_highest_bid = host.highest_bid

    @property
    def current_bid(self):
        return self._current_bid

    @current_bid.setter
    def current_bid(self, v):
        self._current_bid = v

    @property
    def current_highest_bid(self):
        return self._current_highest_bid

    @current_highest_bid.setter
    def current_highest_bid(self, v):
        self._current_highest_bid = v

    def bid(self, amount):
        self.current_bid = amount
        self.publisher.notify(amount)

    def update(self, arg):
        """
        method to bid for a new price
        :param arg: new bid
        :return:
        """
        if arg > self.publisher.highest_bid:
            self.publisher.current_highest_bid_holder = self.name
            self.publisher.highest_bid = arg
            self.current_highest_bid = arg

    def __str__(self):
        return "Bidder: {}, Current bid: {}, Current highest bid: {}".format(self.name,
                                                                             self.current_bid,
                                                                             self.current_highest_bid)


if __name__ == "__main__":
    host = Host("")
    print(host)
    print()

    bidder1 = Bidder("tim", host)
    bidder1.bid(10)
    print(host)
    print(bidder1)
    print()

    bidder2 = Bidder("tom", host)
    bidder2.bid(20)
    print(host)
    print(bidder1)
    print(bidder2)




