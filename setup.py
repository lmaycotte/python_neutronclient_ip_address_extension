import setuptools

setuptools.setup(
    name="python-neutronclient-ip-address-extension",
    version="0.1",
    description="Adds IP address resource support to python-neutronclient",
    long_description="",
    author="Rackspace",
    author_email="",
    url="http://TBD",
    license="Apache License, Version 2.0",
    install_requires=["rackspace-python-neutronclient"],
    py_modules=["python_neutronclient_ip_address_extension"],
    entry_points={
        "neutronclient.extension": [
            "ip_address = python_neutronclient_ip_address_extension"]
    }
)
