from time import sleep


class TrafficLight:
    # attributes
    __color = {'RED': [f'\033[41m RED', 7],
               'YELLOW': [f'\033[43m YELLOW', 3],
               'GREEN': [f'\033[42m GREEN', 5]
               }

    # methods
    @staticmethod
    def running():
        print(f'traffic light is turning on')
        for key in TrafficLight.__color:
            print(TrafficLight.__color.get(key)[0])
            sleep(TrafficLight.__color.get(key)[1])


tl = TrafficLight()
tl.running()
