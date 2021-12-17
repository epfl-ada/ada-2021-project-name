# Hashing out the crypto talk

Datastory: https://epfl-ada.github.io/ada-2021-project-name/ 

## Abstract

Trends in our society are very versatile. They can originate from a specific community or grow from a general opinion. The nature of topics trending at a particular time can reflect the general state of a country or even the world. Some issues can trend for only a few weeks or months while others become an established subject of discussion.      
Among the many subjects that were trending these last few years, Blockchain and cryptocurrency are probably the most recurring. These topics are also one of the most complex to apprehend, and even though they seem hard to tackle, multiple communities rapidly adopted them, from athletes to social media influencers. What seemed at first a topic exclusive to experts became a worldwite buzz.     
The story that we would like to present is about how and why did cryptocurrency and blockchain gain popularity as a hot topic ? Who are the main actors that started this topic, and how did it propagate over different groups?  


## Research questions 

- When did cryptocurrency/blockchain became a popular topic ?
- How did its popularity spread among the different groups (concerning occupations, genders, and age) over the years?
- What are the major events that led to this development ?

## Opportunity for further analysis

Blockchain and cryptocurrency are very heavy topics to present. While we are only going to analyze how they came to grow in popularity and among which groups that happened, a few other questions are worth responding to:
- How did the rise of cryptocurrency affect the political and financial spheres ?
- Who are the communities that welcomed or denied cryptocurrency the most ? 
- Was blockchain/ cryptocurrency responsible for the rise in popularity of other topics ? like cybersecurity for exemple ?

## Dataset 

For this project, we will primarily use:
- The Quotebank dataset, containing over 178 million quotations extracted from 162 million English news articles published between 2008 and 2020. 
- The Wikidata Knowledge Graph, an open knowledge base of over 90 million data items, acts as the structural data for sites such as Wikipedia, Wikisource, and others ...  


## Methods 
When analyzing the data, we will first filter out unnecessary quotations. We do that by keyword matching. We expect cryptocurrency/blockchain to be related to certain buzzwords. This way, we can handle the massive amount of given data - by narrowing our attention to particular quotes.

Then will answer our research questions using data visualizations and descriptive statistics of the dataset. We will examine distributions of interesting keywords in quotations of people from different groups.

We also used Sentence BERT network and T-SNE clustering algorithm for comparing the "meaning" of different quotes

**Data download, filtering, and transformation**  
For end-to-end data preprocessing, run the following command:
```bash
bash download.sh
```
It consists of four main steps:
* Downloading the archived data from `zenodo` and unzipping archives
* Transformation of the data and selecting the quotes relevant to `bitcoin`, `crypto`, and related topics with `preprocess.py`.
* Merging data with `WikiData` with `merge.py`.
* Collecting vocabularies to match `WikiData` ids to human-readable entities with `build_vocab.py`.

\*During the preprocessing we noted that there were quite a lot of people with no occupation.  In our case this meant that they don’t actually have a wiki page. And this in turn meant that they were not famous. We had to google those people by hand, and add their occupations from «linked.in» «Facebook», and potentially other sources… This cost us quite some time……

We’ve also merged by hand quite a lot of occupations into bigger groups. For example all the potential sports, manager positions, different types of business, media activity and so on…

## Organization:

- **Narek Alvandian**. Data preprocessing and analysis, Machine Learning programming, potentially WEB development.
- **Amine Tourki**. Notebook and report writing, Problem formulation, Analysis, and extraction of results, Coding up the algorithm, Visualizations, and plots.
- **Maksim Zubkov**. Data cleaning and preprocessing, Machine Learning programming, WEB development, Design.
- **Emna Tourki**. Analysis and extraction of results, Running tests, Notebook and report writing, Cleaning and commenting on the code.

## Proposed Timeline

- Week1: 15.11.2021 - 21.11.2021
    * Decide on the data to analyse and datasets to use. 
    * Solve specific problems related to our dataset(Find the actual speaker from the list of all matches from WikiData, etc).

- Week2: 22.11.2021 - 28.11.2021
    * Form a concrete idea on how we would like our data story to look like.
    * Running tests on dataset, answering our research questions.
    * Analysis and extraction of results(notebook).

- Week3: 29.11.2021 - 05.12.2021
    * Decide and design our result visualizations.
    * Use the selected results (with creative visuallization) to implement a first version of the data story (this includes creating the HTML template, CSS files and other requirements for the web page).

- Week4: 06.12.2021 - 12.12.2021
    * Implementation of the final data story.

- Week5: 13.12.2019 - 17.12.2019
    * General testing.
    * Small design refinements and last minute fixes.
