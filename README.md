# :wave: Welcome to Snapshot module v1

This module can create snapshots of the state of the system each 5 minutes:

- :white_check_mark: 	Overall CPU load 
- :white_check_mark:  Overall memory usage 
- :white_check_mark:  Overall virtual memory usage 
- :white_check_mark:  IO information 
- :white_check_mark:  Network information 


# Installation

- :point_right: At first download module "Snapshot" into installaton directory 
- :point_right: Secondary run "pip install ."

# Usability

For correct module work you must input 2 arguments:
- :point_right: '-f', '--file' type of output file txt or json
- :point_right: '-s', '--sec'  time beetween snapshots in sec (default 300)

For example 'snapshot -s 5 -f txt' (time between snapshots 5 second, type of outup file is *.txt) or 'snapshot -s 60 -f json' (time between snapshots 60 second, type of outup file is *.json)

# Uninstall and questions

- :point_right: run "pip uninstall snapshot"
- :point_right: mail to author Anton_Antanovich@epam.com
