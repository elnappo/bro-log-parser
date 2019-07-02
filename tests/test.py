import glob
import unittest

import brologparse


class TestBroLogParse(unittest.TestCase):
    def setUp(self):
        self.log_dir = "tests/logs/*.log"

    def test_blackbox_parse_file(self):
        log_files = glob.glob(self.log_dir)
        self.assertGreater(len(log_files), 1)

        for log_file in log_files:
            print(log_file)
            with self.subTest(i=log_file):
                with open(log_file, "r") as f:
                    for i in brologparse.parse_log(f):
                        pass

    def test_blackbox_parse_file_log(self):
        log_files = glob.glob(self.log_dir)
        self.assertGreater(len(log_files), 1)

        for log_file in log_files:
            with self.subTest(i=log_file):
                    for i in brologparse.parse_log_file(log_file):
                        pass
