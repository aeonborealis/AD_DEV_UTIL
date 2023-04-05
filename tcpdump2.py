import subprocess

# Define the tcpdump command with desired options
command = ['tcpdump', '-i', 'eth0', '-n']

# Start tcpdump process and capture output
process = subprocess.Popen(command, stdout=subprocess.PIPE)

# Read and print output line by line
while True:
    output = process.stdout.readline()
    if output == b'' and process.poll() is not None:
        break
    if output:
        print(output.strip())
