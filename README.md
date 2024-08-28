# collada2obj

This Python library can be used to easily convert collada (i.e., `.dae`) files
to wavefront (i.e., `.obj` ) files. This transformation between file formats for 3d
models is useful for a variety of applications, though this library was motivated
by the need for this transformation in some robotics applications.

At the moment, this library is a work in progress and is not yet fully functional.
However, the basic functionality is there and the library can be used to convert
simple collada files to obj files.

See the `examples` directory for example usages of the library.

## Installation

To install this library, you can use `pip`:

```bash
pip install collada2obj
```

### Local Installation

If you want to install this library locally, you can clone this repository and
install it using `pip` in the following way: Change to the root directory of this repo
and then run the following command:
 
```bash
pip install -e .
```

## Usage

```python
from collada2obj import ColladaFileConverter

def main(input_filename: str = "../convert_base_mesh/base.dae", output_filename: str = "./out.obj"):
    # Setup
    print(
        "Create a converter for the Collada file \"{}\" and export to OBJ file \"{}\"."
        .format(input_filename, output_filename)
    )
    converter = ColladaFileConverter(dae_filename=input_filename, obj_filename=output_filename)
    converter.export_obj()

```