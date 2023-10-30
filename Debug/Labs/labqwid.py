"""from multiprocessing import Pool
import os
import subprocess
src = "/home/student-00-d86013fcc87c@linux-instance:/data/prod"
dirs = next(os.walk(src))[1]


def backingup(dirs):
    dest = "/home/student-00-d86013fcc87c@linux-instance:/data/prod_backup"
    subprocess.call(["rsync", "-arq", src+'/'+dirs, dest])

p = Pool(len(dirs))
p.map(backingup(dirs))

"""
"""
#!/usr/bin/env python3
from multiprocessing import Pool
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
"""

import subprocess
from multiprocessing import Pool
import os

global src
src = "{}/data/prod/".format(os.getenv("HOME"))


def sync_data(folder):
    dest = "{}/data/prod_backup/".format(os.getenv("HOME"))
    subprocess.call(["rsync", "-arq", folder, dest])
    print("Handling {}".format(folder))


if __name__ == "__main__":
    folders = []
    root = next(os.walk(src))[0]
    dirs = next(os.walk(src))[1]

    for dir in dirs:
        folders.append(os.path.join(root, dir))

    pool = Pool(len(folders)) if len(folders) != 0 else Pool(1)
    pool.map(sync_data, folders)