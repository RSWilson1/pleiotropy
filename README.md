# Pleiotropy
Calculating pleiotropy for Finngen dataset
The main work for this project is in `pleoitropy_all_chrs.ipynb`, there is an additional script for generating the summary plot figure in `summary_plot.py`. Slides presented are included in the repository.
`explore_finngen.ipynb` was used as the basis for the analysis importing the study loci table and study index.

## Processing of the data
![image](https://github.com/RSWilson1/pleiotropy/assets/30113563/9f665790-73ef-43dc-b8da-efb17e4c05d2)

## Generating clusters
For generating the clusters, the P-Values for all Study Loci were ordered by most-significant and then
using a for-loop all colocalised loci where included (unless already assigned to group of more significant loci).
These were saved as dataframes to help with memory utilisation and accessed again for plotting.

## Results
See slides in repository.


## Future development
- Remove related EFO terms to estimate a better proxy for specificity, estimating distance between EFO terms would be useful possibly by network connections?
- Create a quantitative score for specificity.
- Integrate into gentropy for optimising L2G scores? Or another score for indicating off-target effects?
- Link to Locus2Gene Scores.
- Investigate any other interesting clusters.
