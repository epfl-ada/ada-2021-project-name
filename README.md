# What's trending ?
 
## Abstract

Trends in our society are very versatile. They can originate from a specific community or grow from a general opinion. The nature of topics trending at a certain time can reflect the general state of a country or even the world. Some topics can trend for only a few weeks or months while others become an established subject of discussion.  
A trending topic can also propagate from country to country or from group to group. It can be very hard to predict what will happen to a given trend at a certain point. Will it grow ? will it halt ? for how long will this trend stay ?   
The story that we would like to present is about how trends in our society propagate. Who are the main actors that led a certain topic to trend and how that trend propagated over the different groups of persons.  
Given the extensive amount of worldwide trends over the past years, this project will tackle only a few trends (blockchain,global warming...) and analyse their propagation in our society.


## Research questions 

- When did the trend start and from which group of people ?
- How did the trend spread among the different groups (with respect to occupations , genders and age) and over the years ?
- Given a trend, can we detect when its major events occurred?

## Opportunity for further analysis

Given the scale of this project, we will only be able to respond to a few but major questions. Additional interesting research questions include: 
- How did the genral opinion over a trend affect its propagation ? 
- Can a trend be the consequence of another trend ? 

## Dataset 

For this project we will primarly use:
- The Quotebank dataset, which contains over 178 million quotations extracted from 162 million English news articles published between 2008 and 2020. 
- The Wikidata dataset, an open knowledge base of over 90 million data items that acts as the structural data for sites such as Wikipedia, Wikisource and others...  

(Potential dataset: google trends)

## Methods 

### Data download, filtering, and transformation
For end-to-end data preprocessing, run the following command:
```bash
bash download.sh
```
It consists of four main steps:
* Downloading the archived data from `zenodo` and unzipping archives
* Transformation of the data and selecting the quotes relevant to `bitcoin`, `crypto`, and related topics with `preprocess.py`.
* Merging data with `WikiData` with `merge.py`.
* Collecting vocabularies to match `WikiData` ids to human-readable entities with `build_vocab.py`.

### Rest of the methods !!!!!!!!!!

## Organization:
---
- **Narek Alvandian**:Basic structure of repo and notebook, Analysis and extraction of results, Machine Learning programming, Coding up the algorithm.
- **Amine Tourki**:Notebook and report writing, Problem formulation, Analysis and extraction of results, Coding up the algorithm, Visualizations and plots.
- **Maksim Zubkov**: Data cleaning and preprocessing, First hands on with the dataset, Cleaning and commenting the code,Website design.
- **Emna Tourki**:Analysis and extraction of results, Running tests, Notebook and report writing, Cleaning and commenting the code.




