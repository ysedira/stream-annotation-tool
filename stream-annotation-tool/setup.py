from setuptools import setup

setup(
    name='stream_annotation_tool',
    packages=['api', 'vocals', 'settings'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)
