from setuptools import setup, find_packages

setup(
    name='photo_mover',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'watchdog',
    ],
    entry_points={
        'console_scripts': [
            'photo-mover=photo_mover.mover:start_monitoring',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A script to move photos from the Downloads directory to the Photos directory',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/photo_mover',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
