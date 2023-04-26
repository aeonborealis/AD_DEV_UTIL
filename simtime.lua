import time

# Define a function to simulate virtual time
def virtual_time_simulation():
    start_time = time.time()
    virtual_time = 0
    
    # Loop to simulate virtual time
    while virtual_time < 10:
        virtual_time = time.time() - start_time
        print(f"Virtual Time: {virtual_time}")
        time.sleep(1)

# Call the virtual_time_simulation() function
virtual_time_simulation()
