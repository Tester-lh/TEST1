import selenium

class Maxi(object):
    def __init__(self,browser='firefox'):
        if browser=='firefox':
            self.driver=webdriver.Fire