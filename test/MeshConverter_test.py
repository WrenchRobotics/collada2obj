"""
MeshConverter_test.py
Description
-----------
This file contains tests for the MeshConverter class.
"""

from importlib import resources as impresources
import unittest
import xml.etree.ElementTree as ET

# Local imports
import collada2obj
from collada2obj import MeshConverter

class TestMeshConverter(unittest.TestCase):
    def test_determine_sources_technique_common1(self):
        """
        Description
        -----------
        This test checks the determine_sources_technique_common method.
        :return:
        """
        # Setup

        dae_filename = str(
            impresources.files(collada2obj) / "../examples/convert_base_mesh/base.dae"
        )
        tree = ET.ElementTree(file=dae_filename)

        # FIX xmlns problem
        # http://stackoverflow.com/questions/13412496/python-elementtree-module-how-to-ignore-the-namespace-of-xml-files-to-locate-ma
        for el in tree.iter():
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]  # strip all namespaces

        meshes = tree.findall('library_geometries/geometry/mesh')

        # Algorithm
        converter = MeshConverter(meshes[0])
        source0 = converter.sources[0]

        accessor0 = source0.find("technique_common").find("accessor")

        # Test
        tc = converter.determine_sources_technique_common(source0)

        self.assertEqual(tc.source, source0.attrib["id"])
        self.assertEqual(tc.count, int(accessor0.attrib["count"]))
        self.assertEqual(tc.stride, int(accessor0.attrib["stride"]))


if __name__ == '__main__':
    unittest.main()