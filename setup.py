from setuptools import setup, find_packages

if __name__ == "__main__":
    setup(
        name="kafkahelpers",
        version="0.0.1",
        description="Helpers for aiokafka clients",
        url="https://github.com/jhjaggars/kafkahelpers",
        author="Jesse Jaggars",
        author_email="jhjaggars@gmail.com",
        packages=find_packages(),
        install_requires=[
            "kafka-python",
            "attr",
        ],
        package_data={'': ['LICENSE']},
        license='Apache 2.0',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.6'
        ],
        include_package_data=True
    )
