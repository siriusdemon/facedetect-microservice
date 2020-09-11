import setuptools


setuptools.setup(
    name = "centerface",
    version = "1.0.0",
    author = "sirius demon",
    author_email = "mory2016@126.com",
    description="centerface",
    long_description="centerface",
    long_description_content_type='text/markdown',
    url = "https://github.com/siriusdemon/private/",
    packages=setuptools.find_packages(),
    package_data = {
        'centerface': ['centerface.onnx'],
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)