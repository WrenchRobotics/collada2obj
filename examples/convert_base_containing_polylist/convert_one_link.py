from functools import reduce
import ipdb
import typer
import xml.etree.ElementTree as ET
import numpy as np

# Local imports
from collada2obj import ColladaFileConverter


def main(input_filename: str = "./base.dae", output_filename: str = "./out.obj"):
    # Setup
    print(
        "Create a converter for the Collada file \"{}\" and export to OBJ file \"{}\"."
        .format(input_filename, output_filename)
    )
    converter = ColladaFileConverter(dae_filename=input_filename, obj_filename=output_filename)
    converter.export_obj()


if __name__ == '__main__':
    with ipdb.launch_ipdb_on_exception():
        typer.run(main)
