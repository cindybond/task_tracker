from setuptools import setup, find_packages

setup(
    name="task-tracker",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'task-cli=task_tracker.main:main'
        ],
    },
    install_requires=[],
)
