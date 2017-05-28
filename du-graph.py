#!/usr/bin/env python
import sys
import subprocess

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0;0m"


class dirEntry:
    def __init__(self, dirname, size):
        self.dirname = dirname
        self.size = size
 
 
def get_terminal_width():
    command = ['tput', 'cols']
    try:
        width = int(subprocess.check_output(command))
    except OSError as e:
        print("Invalid Command '{0}': exit status({1})".format(command[0], e.errno))
        print("[info] no tput found. assuming width = 80 columns")
        return 80
    except subprocess.CalledProcessError as e:
        print("Command '{0}' returned non-zero exit status: ({1})".format(command, e.returncode))
    else:
        return width
 
 
def display_graph(my_dirs, tty_width):
    total_size = int(my_dirs[0].size)
    unit = 'Kb'
    if total_size > 1000 and total_size < 1000000:
        unit = 'Mb'
    elif total_size > 1000000:
        unit = 'Gb'
    sys.stdout.write (GREEN)

    if unit == 'Mb':
        print("[info] {0} total size: {1:.3f} {2}".format(my_dirs[1].dirname, float(my_dirs[1].size) / 1000, unit))
    elif unit == 'Gb':
        print("[info] {0} total size: {1:.3f} {2}".format(my_dirs[1].dirname, float(my_dirs[1].size) / 1000000,unit))
    else:
        print("[info] {0} total size: {1} {2}".format(my_dirs[1].dirname, my_dirs[1].size, unit))
    sys.stdout.write (RESET)
    print ("")
    if len(my_dirs) == 2:
        sys.stdout.write(YELLOW)
        print ("Buddy, there are no entries in this directory tree.")
        sys.stdout.write (RESET)
        return False
    sys.stdout.write (YELLOW)
    print('{0:70} || {1:10s} {2:10s}'.format('directory', 'size', 'usage perc'))
    print ("")
    sys.stdout.write (RESET)
    tot_cars = tty_width - 6
    for each in my_dirs[-(len(my_dirs)-2):]:
        perc = (float(each.size) / total_size) * 100
        curr_cars = int(round (( perc * tot_cars ) / 100,0))
        if unit == 'Gb':
            print('{0:70} => {1:10.3f} {2}   {3:.2f} %'.format(each.dirname, float(each.size)/1000000, unit, perc))
        elif unit == 'Mb':
            print('{0:70} => {1:10.3f} {2}   {3:.2f} %'.format(each.dirname, float(each.size)/1000, unit, perc))
        else:
            print('{0:70} => {1:10s} {2:.2f} %'.format(each.dirname, each.size, perc))
        sys.stdout.write("[ ")
        if perc >= 70.0:
            sys.stdout.write(RED)
        else:
            sys.stdout.write(BLUE)
        for i in range (tot_cars):
            if i <= curr_cars:
                sys.stdout.write("|")
            else:
                sys.stdout.write(" ")
        sys.stdout.write(RESET)
        sys.stdout.write(" ]\n")
        sys.stdout.flush() 

def main():
    my_dirs = []
    read_stdin(my_dirs)
    tty_width = get_terminal_width()
    display_graph(my_dirs, tty_width)
 
 
def read_stdin(my_dirs):
    for line in sys.stdin:
        entry=line.rstrip()
        entry_arr =  entry.split('\t')
        entry_to_add = dirEntry(entry_arr[1], entry_arr[0])
        my_dirs.append(entry_to_add)
 
 

if __name__ == "__main__":
    main()


