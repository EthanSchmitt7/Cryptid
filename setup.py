import sys
from pathlib import Path
from shutil import copyfile

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py

install_requires = []
dev_requires = ["black", "pylint", "isort", "wheel"]


EXT_MODULES = {}
INCLUDE_DIRS = {}
CMD_CLASS = {}
if sys.argv[1] == "build_ext":
	import numpy
	from Cython.Build import cythonize
	from Cython.Distutils import build_ext

	EXT_MODULES = cythonize(["src/**/*.py"], compiler_directives={'language_level': "3", "nonecheck": True, "boundscheck": False}, build_dir="./build")

	INCLUDE_DIRS = [numpy.get_include()]

	class BuildExt(build_ext):
		def run(self):
			super().run()

			for f in Path("src/").glob("**/__init__.py"):
				f_path = Path(self.build_lib) / Path(*f.parts[1:])
				f_path.parent.mkdir(parents=True) if not f_path.parent.exists() else ...
				copyfile(f, f_path)

	class BuildPy(build_py):
		def build_packages(self):
			pass

	CMD_CLASS = {"build_ext": BuildExt, "build_py": BuildPy}

setup(
	name="cryptid",
	version="0.1.0.dev0",
	description="ECS Framework",
	python_requires=">=3.10.0",
	packages=find_packages("src"),
	package_dir={"": "src"},
	install_requires=install_requires,
	extras_require={"dev":dev_requires},
	include_package_data=True,
	ext_modules=EXT_MODULES,
	cmdclass=CMD_CLASS,
	include_dirs=INCLUDE_DIRS
)