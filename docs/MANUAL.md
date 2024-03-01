# Manual

## Operation

To run my_application
In the enviroment terminal (see INSTALLATION.md on how to create and activate the required environment and dependencies)

```bash
$ python __main__.py
```

You will be prompted with questions you need to answer. Please type the answers as instructed by the console to avoid errors.
The console will prompt you to re-enter answers if they are not acceptable or if any error is generated.

Some answers are case insensitive for example: The first prompted question prompted to choose the type of variant description you have. This can be answered as E or e for Ensemble and R or r for Refseq.

The chose allele prompt is also case insensitive, however, this can only take one allele at a time. The functionality to request multiple allele variants is under development! For now, please restart the application and choose another allele variant to get the annotation for each allele.

The data can be viewed as application/json or text/xml. Once the data retrieval is successful, you will be prompted to eneter how you wish to view the file. Please enter the answer as directed by the console to avoid errors.



## Additional resources
The application makes requests to the following APIs. Please read the documentation provided by each API to understand how the application requests data from them and the parameters expected:
Variant Recoder - https://rest.ensembl.org/documentation/info/variant_recoder
Variant Validator - https://variantvalidator.org/
Variant Effect Predictor - https://rest.ensembl.org/documentation/info/vep_hgvs_get
