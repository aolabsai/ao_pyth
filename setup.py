from setuptools import setup, find_packages

setup(
    name="ao_pyth",
    version="0.1.6.1",
    description="AI systems that learn like us, developed by aolabs.ai",
    long_description="docs.aolabs.ai",
    url="https://github.com/aolabsai/ao_python",
    author="AO Labs",
    author_email="eng@aolabs.ai",
    include_package_data=True,
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(exclude=["tests", "tests.*"]),   # maybe change this to match https://stackoverflow.com/questions/14417236/setup-py-renaming-src-package-to-project-name
    install_requires=[
        "requests",     
    ],
    zip_safe=False,
    classifiers=[
        "Private :: Do Not Upload",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
    ],
)