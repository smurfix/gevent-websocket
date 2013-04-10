from setuptools import setup, find_packages


version = __import__('geventwebsocket').get_version()

setup(
    name="gevent-websocket",
    version=version,
    url="https://bitbucket.org/Jeffrey/gevent-websocket",
    author="Jeffrey Gelens",
    author_email="jeffrey@noppo.pro",
    description=("Websocket handler for the gevent pywsgi server, a Python "
                 "network library"),
    long_description=open("README.rst").read(),
    download_url="https://bitbucket.org/Jeffrey/gevent-websocket",
    install_requires=("gevent", "greenlet"),
    packages=find_packages(exclude=["examples", "tests"]),
    license="BSD",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
