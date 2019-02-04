# pcu_keyphrase (Keyphrase extraction for PCU project)

Keyphrase extraction component (kleis) for PCU project.
From a text, extract its keyphrases.

Based on the keyphrase extraction algorithm [kleis][kleis].

![keyphrase](https://framapic.org/mEJuLct7M2MD/Ks9ztUt8pqO3.png)

----

[Check PCU project][pcu].

[pcu]: https://github.com/zevio/pcu_core
[kleis]: https://github.com/sdhdez/kleis-keyphrase-extraction

## Installation

To install requirements, go to pcu_keyphrase/ directory and execute the Makefile with the following command line :

`make init`

## Usage in another project

If you wish to import this module in another Python project, please install it :

`pip install pcu-keyphrase`

Then, add this import line at the beginning of your Python file :

`from pcu_keyphrase import pcu_keyphrase`

You can now use pcu_keyphrase's functions, for example :

`pcu_keyphrase.extractKeyphrases(text)`

## Test

To test your installation, go to pcu_keyphrase/ directory and execute the Makefile with the following command line : 

`make test`
