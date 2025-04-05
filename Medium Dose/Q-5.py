Function to convert Euler angles (yaw, pitch, roll) to quaternion
    import math
    def quaternion(yaw, pitch, roll):
    #### Convert degrees to radians
    yaw_rad = math.radians(yaw)    ### Rotation around z-axis
    pitch_rad = math.radians(pitch) ### Rotation around y-axis
    roll_rad = math.radians(roll)  ### Rotation around x-axis
    
    ### Half-angles for quaternion formula
    cy = math.cos(yaw_rad / 2)    ### Cosine of yaw/2
    sy = math.sin(yaw_rad / 2)    ### Sine of yaw/2
    cp = math.cos(pitch_rad / 2)
    sp = math.sin(pitch_rad / 2)
    cr = math.cos(roll_rad / 2)
    sr = math.sin(roll_rad / 2)
    
    ### Quaternion components (w, x, y, z)
    w = cr * cp * cy + sr * sp * sy  ### Real part
    x = sr * cp * cy - cr * sp * sy  ### x-axis component
    y = cr * sp * cy + sr * cp * sy  ### y-axis component
    z = cr * cp * sy - sr * sp * cy  ### z-axis component
    
    ### Return as list, rounded for clarity
    return [round(w, 4), round(x, 4), round(y, 4), round(z, 4)]

    ### Test the function
    yaw = 0    ### Example: no rotation
    pitch = 0
    roll = 0
    result = quaternion(yaw, pitch, roll)

    ### Print results
    print("Converting Earth Rotation to Martian Quaternion:")
    print(f"Input (Yaw, Pitch, Roll): ({yaw}°, {pitch}°, {roll}°)")
    print(f"Quaternion [w, x, y, z]: {result}")

    ### Additional test with rotation
    yaw_test = 90  # 90° yaw
    pitch_test = 0
    roll_test = 0
    result_test = quaternion(yaw_test, pitch_test, roll_test)
    print("\nTest with 90° Yaw:")
    print(f"Input: ({yaw_test}°, {pitch_test}°, {roll_test}°)")
    print(f"Quaternion [w, x, y, z]: {result_test}")
    print("Brick is ready for Mars with Muchiko and Sanchiko!")
