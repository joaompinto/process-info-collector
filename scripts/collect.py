#!/usr/bin/python3
import errno
import json
from glob import glob
from socket import gethostname
from os.path import realpath
from pprint import pprint

COLLECT_SPEC = ["cgroup", "cmdline", "status", "root"]
COLLECT_LINKS = ["exe", "root", "cwd"]


class MissingProcess(Exception):
    pass


def get_proc_data(proc_base, proc_file):
    try:
        filename = proc_base + "/" + proc_file
        with open(filename) as proc_file:
            proc_data = proc_file.read()
    except IOError:  # Process terminated during collection
        raise MissingProcess
    return proc_data

hostname = gethostname()
all_procs = glob('/proc/[1-9]*')
process_list = []
for proc in all_procs:
    process_info = {"hostname": hostname}
    process_info['proc'] = proc
    for collect_field in COLLECT_SPEC:
        try:
            data = get_proc_data(proc, collect_field)
        except MissingProcess:
            continue
        if '\x00' in data:
            data = data.split("\x00")
        elif '\n':
            data = data.split("\n")
        process_info[collect_field] = data
    for collect_field in COLLECT_LINKS:
        link_path = proc+"/"+collect_field
        try:
            process_info[collect_field] = realpath(link_path)
        except OSError as error:
            if error.errno != errno.ENOENT:
                raise
    process_list.append(process_info)
    #pprint(process_info)
print(json.dumps(process_list, indent=4, separators=(',', ':')))