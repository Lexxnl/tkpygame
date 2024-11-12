from setuptools import setup, find_packages

setup(
    name='tkpygame',
    version='0.1.1',
    description='A custom Tkinter-Pygame module.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lex Kimmel',
    author_email='lex.kimmel@gmail.com',
    url='https://github.com/lexxnl/tkpygame',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pygame',        # Adds pygame as a dependency
        'Pillow',        # Adds the PIL library (Pillow) as a dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
