# MACLog - Wi-Fi Based Attendance System

MACLog is a Python-based attendance tracking system that leverages Wi-Fi connectivity and MAC address identification to monitor and log employee attendance in real time. This system ensures seamless and automated attendance tracking for employees within the company's premises.

## Features
- **Real-Time Monitoring**: Tracks employee presence within the company's network.
- **Automated Attendance Logging**: Logs attendance automatically using device MAC addresses.
- **Wi-Fi Dependency**: All devices must connect to the same Wi-Fi network for tracking.

## Prerequisites
Before running the application, ensure you have the following installed:

- Python 3.8 or later
- Required Python libraries:
  - `tkinter` (for the graphical user interface)
  - `tkcalendar` (for date selection in the GUI)
  - `getmac` (for retrieving MAC addresses)
  - `Pillow` (for handling images, if applicable)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/maclog.git
   cd maclog
   ```

2. Install the required libraries:
   ```bash
   pip install tkcalendar getmac Pillow
   ```

3. Ensure that the device running this application is connected to the same Wi-Fi network as the attendees' devices.

## Usage
1. Run the `index.py` file to start the application:
   ```bash
   python index.py
   ```

2. The application will monitor devices connected to the Wi-Fi network and automatically log attendance based on MAC addresses.

## Notes
- Ensure all employees' devices are connected to the same Wi-Fi network as the system running MACLog.
- Attendance is logged in real time and relies on accurate MAC address detection.

## Troubleshooting
- If you encounter a `ModuleNotFoundError` for any library, verify that it is installed correctly using:
  ```bash
  pip install <library-name>
  ```
- If the application does not detect devices, ensure that:
  - All devices are connected to the same Wi-Fi network.
  - The Wi-Fi network allows MAC address visibility.


## Contributions
Contributions are welcome! Feel free to fork this repository, make enhancements, and submit pull requests.
