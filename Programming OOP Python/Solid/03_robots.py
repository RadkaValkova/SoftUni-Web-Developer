class Robot:
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

class Android(Robot):
    def android_senzors_count(self):
        return 4

class Chappie(Robot):
    def chappi_senzors_count(self):
        return 6


def count_robot_senzors(robots:list):
    for robot in robots:
        if isinstance(robot, Android):
            print(robot.android_senzors_count())
        elif isinstance(robot, Chappie):
            print(robot.chappi_senzors_count())


robots_list = [Android('ssss'), Chappie('mmmm')]
count_robot_senzors(robots_list)