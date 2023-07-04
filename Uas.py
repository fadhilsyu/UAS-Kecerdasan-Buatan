from matplotlib import pyplot as plt


class BaseFuzzy():
    def __init__(self):
        self.maximum = 0
        self.minimum = 0

    def up(self, x):
        return (x - self.minimum) / (self.maximum - self.minimum)

    def down(self, x):
        return (self.maximum - x) / (self.maximum - self.minimum)


class Speed(BaseFuzzy):
    def __init__(self):
        super().__init__()
        self.s1 = 40
        self.s2 = 60
        self.s3 = 80
        self.s4 = 100
        self.sn = 120

    def slow(self, x):
        if x < self.s1:
            return 1
        elif self.s1 <= x <= self.s2:
            self.maximum = self.s2
            self.minimum = self.s1
            return self.down(x)
        else:
            return 0

    def steady(self, x):
        if self.s1 <= x <= self.s2:
            self.maximum = self.s2
            self.minimum = self.s1
            return self.up(x)
        elif self.s2 <= x <= self.s3:
            return 1
        elif self.s3 <= x <= self.s4:
            self.maximum = self.s4
            self.minimum = self.s3
            return self.down(x)
        else:
            return 0

    def fast(self, x):
        if x > self.s4:
            return 1
        elif self.s3 <= x <= self.s4:
            self.maximum = self.s4
            self.minimum = self.s3
            return self.up(x)
        else:
            return 0

    def graph(self, value=None):
        plt.figure(figsize=(15, 10))
        x_slow = [0, self.s1, self.s2, self.sn]
        y_slow = [1, 1, 0, 0]
        plt.plot(x_slow, y_slow, label='slow')

        x_steady = [self.s1, self.s2, self.s3, self.s4, self.sn]
        y_steady = [0, 1, 1, 0, 0]
        plt.plot(x_steady, y_steady, label='steady')

        x_fast = [0, self.s3, self.s4, self.sn]
        y_fast = [0, 0, 1, 1]
        plt.plot(x_fast, y_fast, label='fast')

        if value:
            slow_value = self.slow(value)
            steady_value = self.steady(value)
            fast_value = self.fast(value)
            x_param = [0, value, value]
            y_param = [0, slow_value, steady_value]

            plt.plot(x_param, y_param, 'ro-')

        plt.xticks([0, self.s1, self.s2, self.s3, self.s4], [0, self.s1, self.s2, self.s3, self.s4])

        plt.legend(loc='upper left')
        plt.title('Speed [Output]')
        plt.show()


# Contoh Menjalankan Program
speed = Speed()
temperature = 'FREEZE'
pressure_value = 'VERY LOW'

if temperature == 'FREEZE':
    if pressure_value == 'VERY LOW':
        speed_value = 'FAST'
    elif pressure_value == 'LOW':
        speed_value = 'FAST'
    elif pressure_value == 'MEDIUM':
        speed_value = 'STEADY'
    elif pressure_value == 'HIGH':
        speed_value = 'STEADY'
    elif pressure_value == 'VERY HIGH':
        speed_value = 'SLOW'
elif temperature == 'COLD':
    if pressure_value == 'VERY LOW':
        speed_value = 'FAST'
    elif pressure_value == 'LOW':
        speed_value = 'STEADY'
    elif pressure_value == 'MEDIUM':
        speed_value = 'STEADY'
    elif pressure_value == 'HIGH':
        speed_value = 'STEADY'
    elif pressure_value == 'VERY HIGH':
        speed_value = 'SLOW'
elif temperature == 'WARM':
    if pressure_value == 'VERY LOW':
        speed_value = 'FAST'
    elif pressure_value == 'LOW':
        speed_value = 'STEADY'
    elif pressure_value == 'MEDIUM':
        speed_value = 'STEADY'
    elif pressure_value == 'HIGH':
        speed_value = 'STEADY'
    elif pressure_value == 'VERY HIGH':
        speed_value = 'SLOW'
elif temperature == 'HOT':
    if pressure_value == 'VERY LOW':
        speed_value = 'FAST'
    elif pressure_value == 'LOW':
        speed_value = 'STEADY'
    elif pressure_value == 'MEDIUM':
        speed_value = 'STEADY'
    elif pressure_value == 'HIGH':
        speed_value = 'SLOW'
    elif pressure_value == 'VERY HIGH':
        speed_value = 'SLOW'

print('Speed:', speed_value)

speed.graph()