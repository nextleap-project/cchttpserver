import os
from setuptools import setup

def main():
    with open(os.path.join("blockservice.py")) as f:
        for line in f:
            if "__version__" in line.strip():
                version = line.split("=", 1)[1].strip().strip('"')
                break

    with open("README.rst") as f:
        long_desc = f.read()

    setup(
        name='blockservice',
        description='serve self-authenticating http blockstore',
        long_description = long_desc,
        version=version,
        url='https://blockservice.readthedocs.io',
        license='MIT license',
        platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
        classifiers=['Development Status :: 3 - Alpha',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: POSIX',
                     'Operating System :: MacOS :: MacOS X',
                     'Topic :: Utilities',
                     'Intended Audience :: Developers',
                     'Programming Language :: Python'],
        modules=['blockservice'],
        entry_points={
            "muacrypt": [
                "muacryptcc=muacryptcc.plugin"
            ]
        },
        install_requires=["flask", "flask-httpauth"],
        zip_safe=False,
    )

if __name__ == '__main__':
    main()

