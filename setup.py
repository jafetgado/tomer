import setuptools

with open('README.rst', 'r') as f:
    readme = f.read()

setuptools.setup(
	name='tomer',
	version='0.2',
	author='Japheth Gado',
	author_email='japhethgado@gmail.com',
	description='Predicting enzyme catalytic optimum temperature with ML',
	long_description_content_type='text/x-rst',
	long_description=readme,
	url='https://github.com/jafetgado/tomer',
	keywords='machine-learning enzymes thermostability',
	packages=setuptools.find_packages(),
	include_package_data=True,
	license='GNU GPLv3',
	classifiers=[
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
		'Topic :: Scientific/Engineering'
				],
	install_requires=['numpy', 'pandas', 'scipy', 'scikit-learn', 'joblib'],
	python_requires='>=3'
		)
