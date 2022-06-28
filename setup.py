import setuptools

setuptools.setup(
    name="logsim_rt",
    version="0.1.0",
    url="https://github.com/andymcdgeo/real_time_log_data_simulator",
    author="Andy McDonald",
    description="Experiment to create real time simulations of log data",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv']},
)