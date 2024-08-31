"""
ColladaFileConverter_test.py
Description
-----------
This file contains tests for the ColladaFileConverter class.
"""

from importlib import resources as impresources
import unittest
from os import makedirs

# Local imports
import collada2obj
from collada2obj import ColladaFileConverter

class TestColladaFileConverter(unittest.TestCase):
    def test_determine_sources_technique_common1(self):
        """
        Description
        -----------
        This test checks the determine_sources_technique_common method.
        :return:
        """
        # Setup
        dae_filename = str(
            impresources.files(collada2obj) / "../examples/convert_base_containing_polylist/base.dae"
        )
        converter = ColladaFileConverter(str(dae_filename), obj_filename="./out.obj")

        # Test
        found_company_name = False
        for line in converter.get_preamble_lines():
            found_company_name = found_company_name or ("Wrench Robotics" in line)

        self.assertTrue(found_company_name)

if __name__ == '__main__':
    unittest.main()