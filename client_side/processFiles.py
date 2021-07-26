import subprocess

# PSEUDOGLOBAL VARIABLES; CHANGE THIS DEPENDING ON YOUR CLUSTER
user="pwnedsnk"
down_file_zip="covid_0.zip"
down_file_unzip="covid_00.csv"
up_file="node_0.csv"

# ALSO CHANGE THE VARIABLES OF THE nodeProcessing.py File

# Giving permissions to bash scripts
subprocess.run(["chmod", "+x", "downloadPartition.sh"])
subprocess.run(["chmod", "+x", "startPostgres.sh"])
subprocess.run(["chmod", "+x", "uploadPartition.sh"])
subprocess.run(["chmod", "+x", "stopPostgres.sh"])


# Downloading file
args="./downloadPartition.sh " + user + " " + down_file_zip
subprocess.call(args, shell=True)

# The next command  is to execute Dockerized Postgress
# You can comment if you are not using Postgres
subprocess.call("./startPostgres.sh")

# Process file with python
exec(open("nodeProcessing.py").read())

# Upload Partition
args="./uploadPartition.sh " + user + " " + down_file_unzip + " " + up_file
subprocess.call(args, shell=True)

# StopPostgres
subprocess.call("./stopPostgres.sh")



