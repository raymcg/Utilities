
# Stop Instance after running function

"""
Add this code to end of a python script if you wish to stop the EC2 Instance after running the script.
"""

import os
os.system('sudo shutdown -h now')

