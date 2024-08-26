from setuptools import find_packages, setup
import codecs
import os

if __name__ == "__main__":
    # here = os.path.abspath(os.path.dirname(__file__))
    #
    # with codecs.open(
    #     os.path.join(here, "README.md"), encoding="utf-8"
    # ) as f:
    #     long_description = "\n" + f.read()

    setup(
        name="collada2obj",
        version='{{VERSION_PLACEHOLDER}}',
        author="Kwesi Rutledge",
        author_email="thesolitaryecrivain@gmail.com",
        url="https://github.com/kwesiRutledge/collada2obj",
        # description="A set of convenient logging and testing tools for the Drake robotics toolbox.",
        # long_description_content_type="text/markdown",
        # long_description=long_description,
        packages=find_packages(),
        install_requires=['ipdb', 'typer', 'numpy'],
        keywords=["robotics", "testing", "logging", "dae"],
        # classifiers=[
        #     "Programming Language :: Python :: 3",
        # ]
    )