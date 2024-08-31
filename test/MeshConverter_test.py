"""
MeshConverter_test.py
Description
-----------
This file contains tests for the MeshConverter class.
"""

from importlib import resources as impresources
import numpy as np
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


    def test_find_triangles1(self):
        """
        Description
        -----------
        This test checks the find_triangles method when a mesh does not have the "triangles" tag
        inside the mesh element, but it does have the "polylist" tag.
        :return:
        """
        # Setup
        dae_filename = str(
            impresources.files(collada2obj) / "../examples/convert_base_containing_polylist/base.dae"
        )

        # Extract the mesh
        tree = ET.ElementTree(file=dae_filename)

        # FIX xmlns problem
        # http://stackoverflow.com/questions/13412496/python-elementtree-module-how-to-ignore-the-namespace-of-xml-files-to-locate-ma
        for el in tree.iter():
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]  # strip all namespaces

        meshes = tree.findall('library_geometries/geometry/mesh')

        # Create converter and make sure that it doesn't produce an error when the mesh doesn't have triangles
        converter = MeshConverter(meshes[0])
        triangles = converter.find_triangles()

        # Verify that the number of triangles matches the number listed in the technique_common value
        polylist_elt = meshes[0].find("polylist")

        p_text_str = triangles.find('p').text.split()

        self.assertEqual(
            len(p_text_str) // (3*2),
            int(polylist_elt.attrib['count']))

    def test_find_triangles2(self):
        """
        Description
        -----------
        This test checks the find_triangles method when a mesh does not have the "triangles" or "polylist" tag
        inside the mesh eleemnt.
        :return:
        """
        # Setup
        dae_filename = str(
            impresources.files(collada2obj) / "../examples/convert_base_containing_polylist/base.dae"
        )

        # Extract the mesh
        tree = ET.ElementTree(file=dae_filename)

        # FIX xmlns problem
        # http://stackoverflow.com/questions/13412496/python-elementtree-module-how-to-ignore-the-namespace-of-xml-files-to-locate-ma
        for el in tree.iter():
            if '}' in el.tag:
                el.tag = el.tag.split('}', 1)[1]  # strip all namespaces

        meshes = tree.findall('library_geometries/geometry/mesh')

        # Create converter and make sure that it doesn't produce an error when the mesh doesn't have triangles
        converter = MeshConverter(meshes[0])
        exception_was_raised = False
        try:
            converter.polylist_found = False # Fictitiously set the polylist_found attribute to False
            triangles = converter.find_triangles()
        except Exception as e:
            print(e)
            exception_was_raised = True

        self.assertTrue(exception_was_raised)

if __name__ == '__main__':
    unittest.main()