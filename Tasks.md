
# [] TODO Implement dynamic size and position within the window and each panel
# [X] TODO Add position readouts of current joints
# [X] TODO Center the titles in each panel
# [X] TODO Add buttons to command homing and other commands (zero)
# [] TODO Add serial communication backend
# [] TODO Update the displayed joint positions with the value returned by the firmware after the arm has moved
# [] TODO Make buttons process text and send serial commands when pushed
# [X] TODO Add displays for whether each limit switch is currently pressed or not
# [X] TODO Add a send command button to directly send commands over serial to the arm
# [X] TODO Make LS status displays work with command: "self.statusLight1.SetBackgroundColour('green')"
# [] TODO Make the second tab of the UI into a place to generate poses and queue them, then run the entire queue at once
# [] TODO Make the third tab of the UI a place to save different queues of poses and load them into the second tab to run - possibly also fits in the second tab
# [X] TODO Add a queue in the SerialWrite() function so that for example, when homing, the commands don't get lost before getting sent