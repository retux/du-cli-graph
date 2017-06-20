# du-cli-graph

Example: $ du -kcd 1 /home/start/dir/ | sort -rn | head -n 20 | ./du-graph.py

Or use provided wrapper script:

$ dir-usage.sh /home/matias/ramos_linux/ 20

Usage:

$ dir-usage.sh <initial_directory> <no. of top directories>

