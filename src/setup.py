from setuptools import setup

setup(
    name='aelf',
    version='0.1',
    description='Python SDK for AElf',
    scripts=['helloworld'],
    url='https://github.com/rosona/aelf-sdk.py',
    install_requires=['base58', 'requests', 'coincurve', 'protobuf']
)
