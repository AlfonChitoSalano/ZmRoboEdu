# read here first, https://geekdaxue.co/read/zmrobo@robocode/elb5c7#5kyz7i
import rcu


class SensorColors:
    Red = 1
    Green = 2
    Blue = 3
    Yellow = 4
    Black = 5
    White = 6


# All about motor controller
class MotorController:
    @staticmethod
    def set_motor_straight(speed):
        rcu.SetMotor(1, speed)
        rcu.SetMotor(2, speed)
        rcu.SetWaitForTime(1)
        rcu.SetMotor(1, -speed)
        rcu.SetMotor(2, -speed)
        rcu.SetWaitForTime(1)


# All about color controller
class ColorController:
    _displayTextYellowColor = 0xFFE0
    _screenBackgroundBlackColor = 0x0000

    @staticmethod
    def display_color_in_screen():
        while True:
            display = "Color detected is not either black or white"

            if rcu.GetColorSensor(1, 4) == SensorColors.Black:
                display = "Black color detected"
                rcu.SetDisplayString(1, display, ColorController._displayTextYellowColor,
                                     ColorController._screenBackgroundBlackColor)
                continue

            if rcu.GetColorSensor(1, 4) == SensorColors.White:
                display = "White color detected"
                rcu.SetDisplayString(1, display, ColorController._displayTextYellowColor,
                                     ColorController._screenBackgroundBlackColor)
                continue

            rcu.SetWaitForTime(0.5)

    @staticmethod
    def display_photo_electric_values_in_screen():
        base_color_value = 800

        while True:
            display = str(rcu.GetLightSensor(1)) + " " + str(rcu.GetLightSensor(2)) + " " + str(
                rcu.GetLightSensor(3)) + " " + str(rcu.GetLightSensor(4)) + " " + str(
                rcu.GetLightSensor(5)) + " " + str(rcu.GetLightSensor(6)) + " " + str(
                rcu.GetLightSensor(7))
            rcu.SetDisplayString(1, display, ColorController._displayTextYellowColor,
                                 ColorController._screenBackgroundBlackColor)

            if rcu.GetLightSensor(1) > base_color_value:
                rcu.SetDisplayString(20, "lighter color is detected", ColorController._displayTextYellowColor,
                                     ColorController._screenBackgroundBlackColor)
            else:
                rcu.SetDisplayString(20, " darker color is detected", ColorController._displayTextYellowColor,
                                     ColorController._screenBackgroundBlackColor)

            rcu.SetWaitForTime(0.5)

    @staticmethod
    def display_intelligent_tracking_module_values_in_screen():
        standard_channel_1 = 130
        standard_channel_two = 113
        # ToDo. continue and use these values like the above
        st_channel_three = 103
        st_channel_four = 105
        st_channel_five = 112
        st_channel_six = 118
        st_channel_seven = 101

        while True:
            actual_channel_1 = rcu.GetTraceV2I2C(1, 1)
            actual_channel_2 = rcu.GetTraceV2I2C(1, 2)

            display = str(actual_channel_1) + " " + str(actual_channel_2) + " " + str(
                rcu.GetTraceV2I2C(1, 3)) + " " + str(rcu.GetTraceV2I2C(1, 4)) + " " + str(
                rcu.GetTraceV2I2C(1, 5)) + " " + str(rcu.GetTraceV2I2C(1, 6)) + " " + str(rcu.GetTraceV2I2C(1, 7))
            rcu.SetDisplayString(1, display, ColorController._displayTextYellowColor,
                                 ColorController._screenBackgroundBlackColor)

            display_2 = "values: "

            if actual_channel_1 > standard_channel_1:
                display_2 = display_2 + "light, "
            else:
                display_2 = display_2 + "dark, "

            if actual_channel_2 > standard_channel_two:
                display_2 = display_2 + "light, "

            else:
                display_2 = display_2 + "dark, "

            rcu.SetDisplayString(20, display_2, ColorController._displayTextYellowColor,
                                 ColorController._screenBackgroundBlackColor)
            rcu.SetWaitForTime(0.1)


# entry point
def main():
    # MotorController.set_motor_straight(50)
    # just select between the two both are working
    # ColorController.display_color_in_screen()
    # ColorController.display_photo_electric_values_in_screen()
    ColorController.display_intelligent_tracking_module_values_in_screen()


main()
