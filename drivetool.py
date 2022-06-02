import os
import shutil
r"""
A Windows tool to get information about Drives
"""

def get_drives():
        return [chr(drive) + ":" for drive in range(65, 89) if os.path.exists(chr(drive) + ":")]

def get_space(drive):
    total, used, free = shutil.dsik_usage(drive)

class Drives(list):
    def __init__(self):
        self.extend(get_drives())

    def check_changes(self, overwrite=True):
        new_drives = get_drives()
        changes = {"inserted":[], "removed":[]}
        for drive in new_drives:
            if drive not in self:
                # print("inserted: " + str(drive))
                changes["inserted"].append(drive)
        for drive in self:
            if drive not in new_drives:
                # print("removed: " + str(drive))
                changes["removed"].append(drive)
        if overwrite:
            self.clear()
            self.extend(new_drives)
        return changes

    def get_space(self):
        space = {}
        for drive in self:
            space[drive] = shutil.disk_usage("D:")
        return space

"""
    def check_for_removed(self):
        new_drives = self.get_drives()
        print("self" + str(self))
        print("new_drives: " + str(new_drives))
        for drive in self:
            if drive not in new_drives:
                print("removed: " + drive)
        self = new_drives
        print("self" + str(self))

    def check_for_inserted(self):
        new_drives = self.get_drives()
        for drive in self:
            if drive not in new_drives:
                pass
"""
