## Spack based FairSoft

### Preface

This release of FairSoft will be the last featuring the classic
(or "Legacy") FairSoft installation method.
It is planned to be replaced by a spack based system.
This is currently in an EXPERIMENTAL state, and meant for
early adopters.

### Introduction

The newly released FairSoft modernizes and reorganizes the framework installation.
All needed packages, including the FairRoot package itself,
are now installed using [Spack](https://spack.readthedocs.io/en/latest/).

The packages are installed by Spack automatically using package [recipes](https://spack-tutorial.readthedocs.io/en/latest/tutorial_packaging.html), stored in the corresponding folders of the [packages](./repos/fairsoft/packages) directory. The [recipe](https://spack-tutorial.readthedocs.io/en/latest/tutorial_packaging.html)
lists the dependencies of the given package and describes its installation procedure. A collection of packages that form the software framework is called [spack environment](https://spack.readthedocs.io/en/latest/environments.html)  - examples of such are located in the [env](./env) directories.

In the process of installing of a package, Spack creates its list of dependencies,
forming the so-called installation tree. It is possible to install different packages/versions with [Spack](https://spack.readthedocs.io/en/latest/). Since they share a common installation tree, the Spack reuses already available software when installing new package.


### Table of Contents
* [I. Preparation](preparation.md) (download the package)
* [II. Installation](installation.md) (install packages in environment)
* [III. Execution](execution.md) (using the framework)
* [IV. Development](development.md)
* [V. Troubleshooting](troubleshooting.md)
* [VI. Advanced topics](advanced.md)

#### Appendix:
* [Structure of this repo](structure.md)