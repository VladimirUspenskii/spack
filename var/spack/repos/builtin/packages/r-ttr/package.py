# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RTtr(RPackage):
    """Technical Trading Rules

    A collection of over 50 technical indicators for creating technical trading
    rules. The package also provides fast implementations of common
    rolling-window functions, and several volatility calculations."""

    homepage = "https://github.com/joshuaulrich/TTR"
    url      = "https://cloud.r-project.org/src/contrib/TTR_0.23-1.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/TTR"

    version('0.24.2', sha256='2587b988d9199474a19470b9b999b99133d0d8aa45410813e05c5f0ed763711b')
    version('0.23-4', sha256='eb17604da986213b3b924f0af65c3d089502a658a253ee34f6b8f6caccf6bfa2')
    version('0.23-3', sha256='2136032c7a2cd2a82518a4412fc655ecb16597b123dbdebe5684caef9f15261f')
    version('0.23-1', sha256='699798f06ceae9663da47b67d1bc8679fc1c0776d12afd054d6ac4d19e05b2ae')

    depends_on('r-xts@0.10-0:', type=('build', 'run'))
    depends_on('r-zoo', type=('build', 'run'))
    depends_on('r-curl', when='@0.23-4:', type=('build', 'run'))
