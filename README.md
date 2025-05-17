# Alzheimer's Disease Risk Prediction Using GWAS SNP Data

Graduation project for a Master's degree in Computer Science (June 2025).  
Advisor: Dr. Yasmine Mansour

## 🧠 Project Overview

This project focuses on predicting the risk of Alzheimer’s disease by analyzing SNPs (Single Nucleotide Polymorphisms) using GWAS data in combination with machine learning. The goal is to identify individuals with a higher genetic risk of Alzheimer’s and demonstrate the feasibility of building predictive models based on public genetic and clinical data.

## 📊 Data Sources

- **GWAS Catalog** ([ebi.ac.uk/gwas](https://www.ebi.ac.uk/gwas)) – SNPs associated with Alzheimer’s disease ([Trait: MONDO_0004975](https://www.ebi.ac.uk/gwas/efotraits/MONDO_0004975))
- **NCBI Study** – [PMID: 27770636](https://www.ncbi.nlm.nih.gov/pubmed/?term=27770636)
- **SNP Filtering Method** – p-values thresholds (1e-4, 1e-5, 1e-8) based on [this study](https://www.nature.com/articles/s43856-023-00269-x)
- **ADNI GWAS Data** – Genetic and clinical data from the Alzheimer's Disease Neuroimaging Initiative ([ADNI](https://ida.loni.usc.edu/login.jsp))
- **ADNIMERGE** – Merged clinical and diagnostic dataset across ADNI phases ([example study using ADNIMERGE](https://www.nature.com/articles/s41598-024-51985-w))

## 📁 Data Access

Due to file size, the ADNI GWAS dataset and preprocessing files are not stored in this repository. You can download the data used in this project here:

> 📂 [Download Project Dataset](https://drive.google.com/file/d/12jJcFhQXsJhtVHjm40px43200HDx13n3/view?usp=sharing)

> ⚠️ Note: Access to original ADNI data requires registration and approval via [ida.loni.usc.edu](https://ida.loni.usc.edu/).

## 🧬 Methodology

1. **GWAS Query**: SNPs associated with Alzheimer’s were collected from GWAS Catalog.
2. **Filtering**: SNPs were filtered using different p-value thresholds.
3. **ADNI GWAS Processing**:
   - Raw data in PLINK format (`.bed`, `.bim`, `.fam`)
   - Converted to `.raw` using PLINK for analysis
   - Removed SNPs with missing identifiers or poor quality
4. **Feature Selection**: Matched SNPs between GWAS and ADNI data.
5. **Clinical Merge**: Combined genetic data with phenotype labels from ADNIMERGE.
6. **Modeling**: Applied machine learning techniques to classify risk probability (e.g., high risk = 85%).

## ⚙️ Tools & Technologies

- Python (pandas, numpy, scikit-learn)
- PLINK (genetic data processing)
- Jupyter Notebook
- Git & GitHub



