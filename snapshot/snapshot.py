#!/usr/bin/env python
import psutil
import time
import json
import argparse
import datetime


class Snapshot:
    snaps = 0

    def __init__(self):
        self.time = str(datetime.datetime.now())
        self.name = "SNAPSHOT %d" % Snapshot.snaps
        self.overall_cpu_usage = psutil.cpu_percent(interval=1, percpu=True)
        self.memory_total = str(psutil.virtual_memory().total)
        self.memory_available = str(psutil.virtual_memory().available)
        self.overall_memory_usage = str(psutil.virtual_memory().total - psutil.virtual_memory().available)
        self.vm = str(psutil.virtual_memory().used)
        self.hdd = str(psutil.disk_io_counters())
        self.network = str(psutil.net_io_counters())
        Snapshot.snaps += 1

    def __str__(self):
        return '%s: %s: %s, cpu_percents(%s) %s, %s, %s, %s' % \
               (self.name,
                self.overall_cpu_usage,
                self.memory_total,
                self.memory_available, self.overall_memory_usage,
                self.vm, self.hdd, self.network)


def out_to_json(line: str, name_of_file: str):
    json_file = open(name_of_file, "a")
    print(line, file=json_file)
    json_file.close()


def out_to_txt(line: str, name_of_file: str):
    txt_file = open(name_of_file, "a")
    print(line, file=txt_file)
    txt_file.close()


def logging():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='text',
                        help='file extension txt ot json')
    parser.add_argument('-s', '--sec', type=int, default=300,
                        help='Time for snapshot')

    args = parser.parse_args()
    out_file = args.file
    sleep_time = args.sec

    while True:
        time.sleep(sleep_time)
        if out_to_json == "json":
            out_to_json(json.dumps(Snapshot().__dict__), "log_output.json")
        if out_file == "txt":
            out_to_txt(Snapshot().__str__(), "log_output.txt")
