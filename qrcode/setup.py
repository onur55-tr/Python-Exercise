import setuptools

setuptools.setup(
        name='qrcode',
        version='0.0.1',
        keywords='Qrcode Amazing artistic animated',
        description='Generator for Qr Codes.',
        author='umut',
        author_email='umutdrsn34@gmail.com',
        url='https://github.com/onur55-tr/Python-Exercises/qr',
        download_url='https://github.com/onur55-tr/Python-Exercises/qr',
        install_requires=[
            'image >= 1.5.33',
            'pyqrcode >= 1.2.1',
            'pypng >= 0.0.21'],
        packages=['qr'],
        license='GPLv3',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Operating System :: MacOS',
            'Operating System :: POSIX :: Linux',
            'Operating System :: Microsoft :: Windows',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
            ],
        entry_points={
            'console_scripts': [
                'qr=qr.terminal:main',
                ],
            },
        python_requires=">=3",
        )
        
