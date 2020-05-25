"nmlreader setup module."

def main():

    from setuptools import setup
    from nmlreader import NMLReader as nmlr

    console_scripts = ["nmlreader=nmlreader.__main__:main"]
    install_requires = ["microapp>=0.2.3", "f90nml>=1.2"]

    setup(
        name=nmlr._name_,
        version=nmlr._version_,
        description=nmlr._description_,
        long_description=nmlr._long_description_,
        author=nmlr._author_,
        author_email=nmlr._author_email_,
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],
        keywords="nmlreader",
        include_package_data=True,
        install_requires=install_requires,
        entry_points={ "microapp.apps": "nmlreader = nmlreader"},
        project_urls={
            "Bug Reports": "https://github.com/grnydawn/nmlreader/issues",
            "Source": "https://github.com/grnydawn/nmlreader",
        }
    )

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()
