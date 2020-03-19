# Extract kmers from Coronavirus sequence

Input: As an example, the coronavirus sequence was used. This sequence was obtained from https://www.ncbi.nlm.nih.gov/nuccore/MN908947

Code: Extracts kmers along with their frequency of occurrence in a sequence.

Output: The most frequently occurring kmer and a dictionary of all kmers and their frequencies. 

eg. ATGCTTAGA... : If k = 3, then 3-mers would be ATG, TGC, GCT, CTT, and so on.
#### The result should look like this: {'atg': 4, 'tgc': 2, ...}

