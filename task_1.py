from time import sleep
class TrafficLight:

    def __init__(self, color):
        self.__color = color

    def running(seconds):
        if seconds > 0:
            color = "red"
            print(color)
            sleep(7)
            color = "yellow"
            print(color)
            sleep(2)
            color = "green"
            print(color)
            sleep(3)


a = TrafficLight.running
a(1)
