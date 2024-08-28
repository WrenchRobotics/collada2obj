from functools import reduce
import ipdb
import typer
import xml.etree.ElementTree as ET
import numpy as np

# Local imports
from collada2obj import MeshConverter


def main(input_filename: str = "./base.dae", output_filename: str = "./out.obj"):
    # Setup
    xmlns = "{https://www.collada.org/2005/11/COLLADASchema}"

    # PARSE XML
    tree = ET.ElementTree(file=input_filename)

    # FIX xmlns problem
    # http://stackoverflow.com/questions/13412496/python-elementtree-module-how-to-ignore-the-namespace-of-xml-files-to-locate-ma
    for el in tree.iter():
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]  # strip all namespaces

    # geometry_0
    meshes = tree.findall('library_geometries/geometry/mesh')

    models = []
    for ii, mesh_ii in enumerate(meshes):
        # Setup
        print(f"Processing mesh {ii}...")
        converter_ii = MeshConverter(mesh_ii)

        # Export
        converter_ii.export_obj(output_filename)


if __name__ == '__main__':
    with ipdb.launch_ipdb_on_exception():
        typer.run(main)
