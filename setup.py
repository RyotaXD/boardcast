from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    name='boardcast',
    ext_modules=cythonize(
        Extension(
            name='boardcast',
            sources=['boardcast.cpp'],
            extra_compile_args=['-O3', '-flto', '-fvisibility=hidden'],
            extra_link_args=['-O3', '-flto', '-Wl,--strip-all']
        ),
        compiler_directives={'boundscheck': False, 'wraparound': False, 'initializedcheck': False}
    )
)
