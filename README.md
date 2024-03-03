# **Variant_Annotator**

[![Build Status](http://localhost:8080/buildStatus/icon?job=my_application%2Fmain)](http://localhost:8080/job/my_application/job/main/)

[![codecov](https://codecov.io/gh/0m0kenny/sprint2/graph/badge.svg?token=X2M4J58G37)](https://codecov.io/gh/0m0kenny/sprint2)

## About 
variant_annotator is a software tool that returns predicted effects of a variant on genes, transcripts, and protein sequence.

This software tool is designed to make requests to Ensembl's Variant Effect Predictor (VEP) Rest API from variant description/identifier entered by the user. The user is expected to know what type of variant description they have- Ensembl's variant identifier or Refseq variant description and the species. The genome build and select transcripts are only required if the user enters a variant description from Refseq. If entering variant identifier from Ensembl, the user will need to choose the allelic variant from a list that will be provided by the software.


## Pre-requisites
variant_annotator will work on Linux operating systems.

## Required software:

Python 3.12.0

## License

Please see [LICENSE](https://github.com/0m0kenny/sprint2/blob/main/LICENSE.txt)

For installation instructions please see [INSTALLATION](https://github.com/0m0kenny/sprint2/blob/main/docs/INSTALLATION.md)

## Operation Manuals

Please see [MANUAL](https://github.com/0m0kenny/sprint2/blob/main/docs/MANUAL.md)