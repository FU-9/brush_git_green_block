#!_*_coding:utf-8_*_

import os
import subprocess
import random
import time


class UpdateGit:

    PATH = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        self.file_name = ""

    @staticmethod
    def random_str():
        random_data = "fajskdfjalsfja"
        return random_data

    @staticmethod
    def get_date():
        now_time = time.strftime("%Y-%m-%d")
        return now_time

    def write_file(self):
        self.file_name = self.get_date()
        file_data = self.random_str()
        with open('{path}/file_dir/{name}.txt'.format(path=self.PATH,name=self.file_name),"w") as f:
            f.write(file_data)
            f.close()

    def run_git(self):
        file_status = subprocess.Popen('git status' % self.user_current_dir, shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)

    def run(self):
        print(self.PATH)


if __name__ == "__main__":

    updata_obj = UpdateGit()
    updata_obj.run()