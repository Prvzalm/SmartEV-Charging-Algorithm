// Initialize
available_power = 92
devices = []  // Queue to keep track of devices in order of connection
current_usage = {}  // Store current usage for each device

// Function to handle a new device connection
function connect_device(device_id, requested_power):
    if requested_power > device_max_capacity:
        requested_power = device_max_capacity  // Cap to max device capacity
    
    if available_power >= requested_power:
        available_power -= requested_power
        devices.push(device_id)  // Add device to the queue
        current_usage[device_id] = requested_power  // Set initial usage
        print(f"Device {device_id} connected with {requested_power} units.")
    else:
        print(f"Device {device_id} cannot connect. Insufficient power.")

// Function to handle a device stopping consumption
function disconnect_device(device_id):
    if device_id in current_usage:
        released_power = current_usage[device_id]
        available_power += released_power
        current_usage.remove(device_id)  // Remove device from active list
        devices.remove(device_id)  // Remove device from queue
        print(f"Device {device_id} disconnected, releasing {released_power} units.")
    else:
        print(f"Device {device_id} is not active.")


// Function to handle change in power consumption by an active device
function change_power_consumption(device_id, new_consumption):
    if device_id in current_usage:
        // Calculate the change in power usage
        old_consumption = current_usage[device_id]
        difference = new_consumption - old_consumption

        // Ensure the new consumption does not exceed the max limit
        if new_consumption > device_max_capacity:
            new_consumption = device_max_capacity

        // Check if enough power is available to accommodate the change
        if available_power + difference >= 0:
            // Adjust available power and device consumption
            available_power += difference
            current_usage[device_id] = new_consumption
            print(f"Device {device_id} updated to {new_consumption} units.")
        else:
            print(f"Cannot update power for device {device_id}. Insufficient power.")
    else:
        print(f"Device {device_id} is not active.")

// Function to print the current status of all devices and their power usage
function print_status():
    for device_id in devices:
        print(f"Device {device_id}: {current_usage[device_id]} units")
    print(f"Available power: {available_power} units.")
    
// Example Scenario:

// Device A connects
connect_device('A', 40)  // Device A gets 40 units

// Device B connects
connect_device('B', 40)  // Device B gets 40 units

// Device C connects
connect_device('C', 12)  // Device C gets 12 units (remaining power)

// Device A drops to 20 units
change_power_consumption('A', 20)  // A's consumption drops, C gets more power

// Device B disconnects
disconnect_device('B')  // B disconnects, releasing 40 units of power
