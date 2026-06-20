# ==========================================
# TechTrack Inventory Manager
# Beginner Version (No SQL / No JSON)
# ==========================================

# ------------------------------------------
# Device Class
# Stores information about one device
# ------------------------------------------
class Device:

    # Constructor runs whenever a new device is created
    def __init__(
        self,
        device_id,
        device_type,
        brand,
        model,
        serial_number
    ):

        self.device_id = device_id
        self.device_type = device_type
        self.brand = brand
        self.model = model
        self.serial_number = serial_number

        # List to store repair records
        self.repairs = []

    # Display device information
    def display(self):

        print(f"""
ID: {self.device_id}
Type: {self.device_type}
Brand: {self.brand}
Model: {self.model}
Serial Number: {self.serial_number}
Repairs: {len(self.repairs)}
----------------------------------
""")


# ------------------------------------------
# Inventory Manager Class
# Handles all inventory functions
# ------------------------------------------
class InventoryManager:

    def __init__(self):

        # Stores all device objects
        self.devices = []

        # Load devices from file
        self.load_devices()

    # --------------------------------------
    # Load devices from devices.txt
    # --------------------------------------
    def load_devices(self):

        try:

            file = open("devices.txt", "r")

            for line in file:

                data = line.strip().split(",")

                # Skip bad lines
                if len(data) < 5:
                    continue

                device = Device(
                    int(data[0]),
                    data[1],
                    data[2],
                    data[3],
                    data[4]
                )

                self.devices.append(device)

            file.close()

        except FileNotFoundError:
            return

    # --------------------------------------
    # Save devices to file
    # --------------------------------------
    def save_devices(self):

        file = open("devices.txt", "w")

        for device in self.devices:

            line = (
                f"{device.device_id},"
                f"{device.device_type},"
                f"{device.brand},"
                f"{device.model},"
                f"{device.serial_number}\n"
            )

            file.write(line)

        file.close()

    # --------------------------------------
    # Generate next ID
    # --------------------------------------
    def generate_id(self):

        if len(self.devices) == 0:
            return 1

        highest = max(
            device.device_id
            for device in self.devices
        )

        return highest + 1

    # --------------------------------------
    # Check if serial exists
    # --------------------------------------
    def serial_exists(self, serial):

        for device in self.devices:

            if device.serial_number == serial:
                return True

        return False

    # --------------------------------------
    # Add new device
    # --------------------------------------
    def add_device(self):

        print("""
1) Computer
2) Monitor
3) Printer
""")

        choice = input("Device Type: ")

        types = {
            "1": "Computer",
            "2": "Monitor",
            "3": "Printer"
        }

        if choice not in types:

            print("Invalid Choice")
            return

        brand = input("Brand: ")
        model = input("Model: ")
        serial = input("Serial Number: ")

        if len(serial) < 5:

            print("Serial Number Too Short")
            return

        if self.serial_exists(serial):

            print("Serial Number Already Exists")
            return

        device = Device(
            self.generate_id(),
            types[choice],
            brand,
            model,
            serial
        )

        self.devices.append(device)

        self.save_devices()

        print("Device Added Successfully")

def view_devices(self):

        if not self.devices:

            print(
                "No devices found."
            )

            return

        sorted_devices = sorted(
            self.devices,
            key=lambda x:
            x.device_type
        )

        for device in sorted_devices:

            device.display()

def search_device(self):

        serial = input(
            "Serial Number: "
        )

        for device in self.devices:

            if (
                device.serial_number
                == serial
            ):

                device.display()
                return

        print(
            "Device not found."
        )

def find_device_by_id(
        self,
        device_id
    ):

        for device in self.devices:

            if (
                device.device_id
                == device_id
            ):

                return device

        return None

def update_device(self):

        try:

            device_id = int(
                input(
                    "Device ID: "
                )
            )

        except ValueError:

            print(
                "Invalid ID."
            )

            return

        device = (
            self.find_device_by_id(
                device_id
            )
        )

        if device is None:

            print(
                "Device not found."
            )

            return

        device.brand = input(
            "New Brand: "
        )

        device.model = input(
            "New Model: "
        )

        self.save_devices()

        print(
            "Device updated."
        )

def delete_device(self):

        try:

            device_id = int(
                input(
                    "Device ID: "
                )
            )

        except ValueError:

            print(
                "Invalid ID."
            )

            return

        device = (
            self.find_device_by_id(
                device_id
            )
        )

        if device is None:

            print(
                "Device not found."
            )

            return

        self.devices.remove(
            device
        )

        self.save_devices()

        print(
            "Device deleted."
        )

def add_repair_record(self):

        try:

            device_id = int(
                input(
                    "Device ID: "
                )
            )

        except ValueError:

            print(
                "Invalid ID."
            )

            return

        device = (
            self.find_device_by_id(
                device_id
            )
        )

        if device is None:

            print(
                "Device not found."
            )

            return

        repair = input(
            "Repair Description: "
        )

        device.repairs.append(
            repair
        )

        print(
            "Repair added."
        )

def view_repairs(self):

        try:

            device_id = int(
                input(
                    "Device ID: "
                )
            )

        except ValueError:

            print(
                "Invalid ID."
            )

            return

        device = (
            self.find_device_by_id(
                device_id
            )
        )

        if device is None:

            print(
                "Device not found."
            )

            return

        if not device.repairs:

            print(
                "No repairs."
            )

            return

        print(
            "\nRepair History\n"
        )

        for repair in (
            device.repairs
        ):

            print(
                f"- {repair}"
            )

def generate_report(self):

        total = len(
            self.devices
        )

        computers = 0
        monitors = 0
        printers = 0

        for device in self.devices:

            if (
                device.device_type
                == "Computer"
            ):

                computers += 1

            elif (
                device.device_type
                == "Monitor"
            ):

                monitors += 1

            elif (
                device.device_type
                == "Printer"
            ):

                printers += 1

        print("""
========== REPORT ==========
""")

        print(
            f"Total Devices: {total}"
        )

        print(
            f"Computers: {computers}"
        )

        print(
            f"Monitors: {monitors}"
        )

        print(
            f"Printers: {printers}"
        )

        print("""
============================
""")


def menu():

    print("""
=================================
TECHTRACK INVENTORY MANAGER
=================================

1. Add Device
2. View Devices
3. Search Device
4. Update Device
5. Delete Device
6. Add Repair Record
7. View Repairs
8. Generate Report
9. Exit
""")


def main():

    manager = (
        InventoryManager()
    )

    while True:

        menu()

        choice = input(
            "Select Option: "
        )

        if choice == "1":

            manager.add_device()

        elif choice == "2":

            manager.view_devices()

        elif choice == "3":

            manager.search_device()

        elif choice == "4":

            manager.update_device()

        elif choice == "5":

            manager.delete_device()

        elif choice == "6":

            manager.add_repair_record()

        elif choice == "7":

            manager.view_repairs()

        elif choice == "8":

            manager.generate_report()

        elif choice == "9":

            print("Goodbye.")
            break

        else:

            print(
                "Invalid selection."
            )


if __name__ == "__main__":
    main()
