# from distutils.core import setup
# from Cython.Build import cythonize
# from distutils.extension import Extension

# import os
# import sys
# import numpy

# extension = Extension( name='jsp_bbs',
#                        sources=['jsp_bbs.pyx',
#                                 'c_utils.cpp',
#                                 ],
#                        language="c++",
#                        extra_compile_args=['-std=c++11'],
#                       )

# setup(
#     ext_modules = cythonize(extension),
#     include_dirs=[numpy.get_include()]
# )

# try:
#     print("checking existence of compiled file *.so")
#     if not(os.path.exists('../bin')):
#       os.makedirs('../bin')
#       print("make bin directory")
#     # compile it into  .o file
#     assert os.system("mv *.so ../bin") == 0
# except:
#     if not os.path.exists("./.so"):
#       print("Error building dynamic library of cython")
#       sys.exit(1)
from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import os
import sys
import numpy

# Adjust file extensions and compiler options for Windows
extension = Extension(
    name='jsp_bbs',
    sources=['jsp_bbs.pyx'#,
             'c_utils.cpp'
             ],
    language="c++",
    include_dirs=[numpy.get_include()],
    # Remove unsupported compiler flag for Visual C++
    # extra_compile_args=['c_utils.o'],
)

setup(
    ext_modules=cythonize(extension),
    include_dirs=[numpy.get_include()]
)

try:
    print("Checking existence of compiled file *.pyd")
    if not os.path.exists('../bin'):
        os.makedirs('../bin')
        print("Created bin directory")
    # Move the compiled .pyd file to the bin directory
    assert os.system("move *.pyd ..\\bin") == 0
except Exception as e:
    print("Error building dynamic library of Cython:", e)
    sys.exit(1)
