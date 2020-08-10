# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Flatbuffers(CMakePackage):
    """Memory Efficient Serialization Library
    """

    homepage = "http://google.github.io/flatbuffers/"
    url      = "https://github.com/google/flatbuffers/archive/v1.9.0.tar.gz"

    version('1.11.0', sha256='3f4a286642094f45b1b77228656fbd7ea123964f19502f9ecfd29933fd23a50b')
    version('1.10.0', '3714e3db8c51e43028e10ad7adffb9a36fc4aa5b1a363c2d0c4303dd1be59a7c')
    version('1.9.0', '8be7513bf960034f6873326d09521a4b')
    version('1.8.0', '276cab8303c4189cbe3b8a70e0515d65')


    # Remove unnecessary const qualifier
    # https://github.com/google/flatbuffers/pull/4698
    patch('remove_unnecessary_const_qualifier.patch', when='@1.9.0')

    # Silence false positive "-Wstringop-overflow" on GCC 10.0 to 11.0
    # https://github.com/google/flatbuffers/commit/515a4052a750dfe6df8d143c8f23cd8aaf51f9d7
    patch('silence_false_positive_gcc10_warning.patch', when='@:1.12.0%gcc@10:11')

    def cmake_args(self):
        args=[]
        args.append('-DFLATBUFFERS_BUILD_SHAREDLIB=ON')
        args.append('-DFLATBUFFERS_BUILD_FLATLIB=OFF')
        args.append('-DCMAKE_BUILD_TYPE=Release')
        args.append('-DCMAKE_MACOSX_RPATH=ON')
        return args
