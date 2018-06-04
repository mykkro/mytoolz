from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    long_description=readme(),
    name="mytoolz",
	version="0.1",
	description="Enter package description here",
	classifiers=[
		"Development Status :: 3 - Alpha",
		"License :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Topic :: Miscellaneous :: Utility"
	],
	keywords="python tools",
	url="http://dev/null",
	author="Myrousz",
	author_email="myrousz@gmail.com",
	license="MIT",
	packages=[
		"mytoolz"
	],
	install_requires=[
		"hashids",
		"pyaml",
		"pydicom"
	],
	test_suite="nose.collector",
	tests_require=[
		"nose",
		"nose-cover3"
	],
	entry_points={
		"console_scripts": [
			"mytoolz-hello=mytoolz.command_line:main",
			"mytoolz-remove-accents=mytoolz.command_line:remove_accents_cli",
			"mytoolz-format-json=mytoolz.command_line:format_json_cli"
		]
	},
    include_package_data=True,
	zip_safe=False
)
