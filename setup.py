from setuptools import find_packages, setup

install_requires = []
dev_requires = ["black", "pylint", "isort", "wheel"]


setup(
	name="cryptid",
	version="0.1.0.dev0",
	description="ECS Framework",
	python_requires=">3.10.0",
	packages=find_packages("src"),
	package_dir={"": "src"},
	install_requires=install_requires,
	extras_require={"dev":dev_requires},
	include_package_data=True,
)