
# [X] TODO Add position readouts of current joints
# [X] TODO Center the titles in each panel
# [X] TODO Add buttons to command homing and other commands (zero)
# [X] TODO Add serial communication backend
# [X] TODO Add displays for whether each limit switch is currently pressed or not
# [X] TODO Add a send command button to directly send commands over serial to the arm
# [X] TODO Make LS status displays work with command: "self.statusLight1.SetBackgroundColour('green')"
# [X] TODO Add a queue in the SerialWrite() function so that for example, when homing, the commands don't get lost before getting sent
# [X] TODO Update the displayed joint positions with the value returned by the firmware after the arm has moved
# [X] TODO Write code to send position commands (call Serial.SerialWrite(string))
# [X] TODO Add a button and code to the angle input panel to move all joints to the currently set positions at the same time
# [X] TODO Make buttons process text and send serial commands when pushed
# [X] TODO Write code to regularly send "print pos" and "LS status" regularly to arm to get info
# [X] TODO Write code to check serial buffer and call SerialRead() when there is something available
# [X] TODO Add the ability to control the gripper to the poses queue tab
# [] TODO Get serial running with teensy hardware, then uncomment SerialComms call in PosesQueuePanel and test

# LESS IMPORTANT
# [] TODO Add another tab to UI to set acceleration, max speed, angle range, LS position, etc parameters, etc
# [] TODO Implement dynamic size and position within the window and each panel
# [X] TODO Make the second tab of the UI into a place to generate poses and queue them, then run the entire queue at once
# [X] TODO Make the third tab of the UI a place to save different queues of poses and load them into the second tab to run - possibly also fits in the second tab