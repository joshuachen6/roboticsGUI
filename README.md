# RoboticsGUI

RoboticsGUI is an interactive graphical tool designed to simplify the generation of Road Runner trajectory code for FTC (First Tech Challenge) robots. It provides a visual interface for mapping out robot paths on a field, allowing developers to "drive" the virtual robot and automatically generate the corresponding Java code.

<img width="3051" height="1844" alt="Screenshot_20260505_203830" src="https://github.com/user-attachments/assets/a239290a-e2d1-4dda-819a-1dc5adf7295a" />

## Key Features

- **Real-time Path Visualization**: See exactly where your robot is on the field with a high-accuracy coordinate system.
- **Interactive Controls**: Move the robot using keyboard shortcuts or direct mouse input for precise positioning.
- **Trajectory Generation**: Automatically generates `TrajectorySequence` code compatible with the Road Runner library.
- **Support for Complex Movements**:
    - Axial movements: Forward, Backward, Strafe Left, and Strafe Right.
    - Rotation: Smooth turning with precise angle control.
    - Positional: `lineTo` and `lineToLinearHeading` support.
- **Event Markers**: Easily add displacement markers (functions) and wait durations directly into your trajectory.
- **Configurable Robot Profile**: Customize robot dimensions, movement speeds, and visual debug aids via a configuration file.
- **Export to Clipboard**: Copy the generated Java code directly to your clipboard for use in your Android Studio project.

## Controls

### Movement
- **W / S**: Move Forwards / Backwards.
- **A / D**: Strafe Left / Right.
- **Q / E**: Rotate Left / Right.
- **Shift (Hold)**: Precision mode (reduces movement and rotation speed).

### Actions
- **Enter**: Start recording movements.
- **Space**: Insert a segment break/waypoint.
- **T**: Open a dialog to move the robot to a specific Pose (X, Y, Heading).
- **F**: Add a function call (Displacement Marker) at the current position.
- **R**: Add a sleep/wait duration.
- **Mouse Click**: Perform a `lineTo` movement to the clicked coordinate.

### Utilities
- **Ctrl + Z**: Undo the last movement segment.
- **Ctrl + C**: Clear the entire path and reset the robot to the center.
- **Ctrl + P**: Generate and copy Road Runner code to the clipboard.
- **M**: Toggle between displaying Robot Pose and Mouse Position coordinates.
- **G**: Cycle through debug view modes (Visualizing sensors or rotation radius).

## Configuration

You can customize the application behavior by editing `config.json`. Available settings include:

- `robot_width` / `robot_length`: Dimensions of your robot in inches.
- `robot_speed` / `robot_turn_speed`: Movement sensitivity.
- `font_size`: UI text scaling.
- `lines`: Define custom debug lines relative to the robot's center (useful for visualizing sensor ranges or intake areas).

## Requirements

- Python 3.x
- `pyglet`: For the GUI and rendering.
- `pyperclip`: For clipboard integration.
- `tkinter`: For dialog boxes and notifications.

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Running the Application

Execute the main script to start the GUI:
```bash
python main.py
```
