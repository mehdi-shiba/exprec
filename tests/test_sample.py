from exprec import Experiment
import os.path
import shutil
import unittest


class Test(unittest.TestCase):
    def test_pass(self):
        with Experiment() as experiment:
            uuid = experiment.uuid
            with experiment.open('testfile.txt', mode='w') as fp:
                fp.write('test\n')
        
        experiment_path = os.path.join('.experiments', uuid)
        self.assertTrue(os.path.exists(experiment_path))
        
        # Clean up:
        shutil.rmtree(experiment_path)
