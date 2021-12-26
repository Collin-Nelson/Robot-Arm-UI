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
# [X] TODO Get serial running with teensy hardware, then uncomment SerialComms call in PosesQueuePanel and test
# [X] TODO Add code to deal with data read from serial
# [X] TODO Add methods to set tc1-6 and LS statuses on the AngleDisplayPanel
# [X] TODO Make AngleDisplayPanel pythonic and no errors except passing wrong "self"
# [X] TODO Make AngleInputPanel pythonic and no errors except passing wrong "self"
# [X] TODO Make ConsoleOutput pythonic and no errors except passing wrong "self"
# [X] TODO Make EndEffectorCommand pythonic and no errors except passing wrong "self"
# [X] TODO Make HomeCommand pythonic and no errors except passing wrong "self"
# [X] TODO Make main pythonic and no errors except passing wrong "self"
# [X] TODO Make MainFrame pythonic and no errors except passing wrong "self"
# [X] TODO Make PosesGeneratorPanel pythonic and no errors except passing wrong "self"
# [X] TODO Make PosesQueuePanel pythonic and no errors except passing wrong "self"
# [X] TODO Make Serial pythonic and no errors except passing wrong "self"
# [X] TODO Make TextCommand pythonic and no errors except passing wrong "self"
# [X] TODO Make ZeroCommands pythonic and no errors except passing wrong "self"
# [X] TODO fix erros for wrong "self" in AngleDisplayPanel
# [X] TODO fix erros for wrong "self" in AngleInputPanel
# [X] TODO fix erros for wrong "self" in ConsoleOutput
# [X] TODO fix erros for wrong "self" in EndEffectorCommand
# [X] TODO fix erros for wrong "self" in HomeCommand
# [X] TODO fix erros for wrong "self" in main
# [X] TODO fix erros for wrong "self" in MainFrame
# [X] TODO fix erros for wrong "self" in PosesGeneratorPanel
# [X] TODO fix erros for wrong "self" in PosesQueuePanel
# [X] TODO fix erros for wrong "self" in TextCommand
# [X] TODO fix erros for wrong "self" in ZeroCommands
# [X] TODO fix erros for wrong "self" in Serial - Needs AngleDisplayPanel - How to get the instance of AngleDispalyPanel to serial?
# [X] TODO rework all code to properly use classes and pass around the correct info (class instances) - possibly pass serial down the tree from main?
# [X] TODO fix buttons only being pressable once/getting pressed on startup (possibly related to above or below issue)
# [X] TODO Fix only one joint homing if at least one joint is unchecked
# [X] TODO fix run queue button on second tab of UI
# [X] TODO look at scope of "filename" in PosesQueuePanel
# [X] TODO Make sure the code in the while loop in main() can run in parallel with the app.mainloop() loop - while loop has been moved to serial in on_timer
# [X] TODO fix AngleDisplayPanel not updating
# [X] TODO debug serial communication and ser.in_waiting in the serial_read function
# [X] TODO Make sure the print pos and LS status messages outgoing and incomming aren't displayed in the UI
# [X] TODO make console output on all tabs the same

# LESS IMPORTANT
# [X] TODO Add a status light/display for the end effector
# [] TODO move AngleDisplayPanel to the console output panel of the UI
# [] TODO Add another tab to UI to set acceleration, max speed, angle range, LS position, etc parameters, etc
# [X] TODO Implement dynamic size and position within the window and each panel - NEEDED?
# [] TODO Add logging
# [X] TODO Make the second tab of the UI into a place to generate poses and queue them, then run the entire queue at once
# [X] TODO Make the third tab of the UI a place to save different queues of poses and load them into the second tab to run - possibly also fits in the second tab