import setuptools

with open("README.md", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyvtflib",
    version="0.2.0",
    author="Lassi Säike",
    description="Python bindings for VTFLib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lasa01/pyvtflib",
    packages=["pyvtflib"],
    package_data={
        "pyvtflib": ["bin/x64/VTFLib.dll", "bin/x86/VTFLib.dll"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3"
    ],
    keywords="vtflib vtf valve",
)
