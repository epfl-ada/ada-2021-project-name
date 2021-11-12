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

(Potential additional dataset: google trends)


## Methods 
When analyzing certain trend, we will first filter out unnecessary quotations. We do that by key-word matching. We expect certain trends and topics to be related to certain buzzwords, this way we can handle the huge amount of given data - by narrowing our attention only on certain quotes.

Then will answer our research questions using data visualizations and descriptive statistics of the dataset. We will examine distributions of interesting key-words in quotations of people from different groups.

Given we have time after implementing out main ideas, we are also thinking about using machine learning techniques to solve certain problems.

- Firstly, we want to use word embeddings to find an actual speaker from the list of all matches from WikiData. The problem is, when we try to find additional info on a speaker using wikidata, there are multiple people with the same name and surname. We think we can solve this problem by comparing speaker's embedding to the embedding of the quote. Ideally, if speaker has the occupancy in the area of the quote's meaning - then the according embeddings will be nearby in the vector space
- Secondly, we also think it would be interesting to look at the sentiment analysis of the quotes, and make visualizations of different statistics, related to the sentiment.


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

- **Narek Alvandian**. Data preprocessing and analysis, Machine Learning programming, potentially WEB development.
- **Amine Tourki**. Notebook and report writing, Problem formulation, Analysis and extraction of results, Coding up the algorithm, Visualizations and plots.
- **Maksim Zubkov**. Data cleaning and preprocessing, Machine Learning programming, WEB development, Design.
- **Emna Tourki**. Analysis and extraction of results, Running tests, Notebook and report writing, Cleaning and commenting the code.

## Proposed Timeline



