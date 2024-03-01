#About my_application
my_application is a software tool that returns transcript annotation based on variant description/identifier provided by the user.
The software tool designed to make requests to Ensembl's Variant Effect Predictor (VEP) rest API from variant description/identifier enetered by the user. The user is expected to know what type of variant description they have- Ensembl's variant identifier or Refseq variant description. Based on the type of description, the software sends a request to either Ensembl's Variant Recoder Rest API or VaraintValidator and parse the data to collect the hgvsg notation. This notation is required for a request to be sent to VEP. Other required information about the variant are the species, genome build and select transcripts. The genome build and select transcripts are only required if the user enters a REfseq Variant description. 

The ensembl variant recoder rest api returns allele variants of the variants, therefore, the user is also required to choose only one allelic variants to get the annotations of.

