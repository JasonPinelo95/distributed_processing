# Big Data Management   Data 5A
# Emmanuel Alejandro Hurtado Alejandre
# Jason Maximiliano Pinelo Hau
# Pedro Alejandro Uicab Díaz

# Script to split the covid.csv into subfiles, it calls bash scripts that
# actually split the files

import subprocess

# Giving permissions to bash  scripts
subprocess.run(["chmod", "+x", "downloadCovid_db.sh"])
subprocess.run(["chmod", "+x", "split_files.sh"])
subprocess.run(["chmod", "+x", "removeOldFiles.sh"])
subprocess.run(["chmod", "+x", "checkfiles.sh"])

# Downloading file
subprocess.call("./downloadCovid_db.sh")

# Splitting file
subprocess.call("./split_files.sh")

# Waiting for new files
subprocess.call("./checkfiles.sh")

# Removing Files
subprocess.call("./removeOldFiles.sh")

