from setuptools import setup

version = {}
with open("bulkvis/_version.py") as fh:
    exec(fh.read(), version)

install_requires = [
    "bokeh~=2.1.0",
    "h5py",
    "pandas~=1.0.5",
    "tornado~=6.0.4",
    "tqdm~=4.46.1",
    "readpaf",
]

setup(
    name="bulkvis",
    version=version["__version__"],
    author="Alexander Payne",
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "bulkvis=bulkvis.bulkvis:main",
        ],
    },
    packages=["bulkvis"],
    python_requires=">=3.6",
    include_package_data=True,
)
