## What's trending?

- Talk about bitcoin, cryptocurrencies cryptography, how popular it is, what big concepts it holds, and the fact that it is such a complicated technical thing, yet everyone is approximately aware of the ideas and how it works, and what it does and so on. 
- Then state that we have the number of questions to answer

1) How did the trend spread among the different groups (concerning occupations, genders, and age) over the years?

- Who was the first one mentioning 
    - here we show the occupations of people who did the first 10 mentions let’s say
    - Then we talk a little about the results 

- What is the distribution over time 
    - here we show the graph of different occupations
    - Then we talk a little about the results 
  
{% include  quotes_by_occupation_slider_years.html %}

2) When were the most «Popularity growing» events

- Show the graph with the shifted quote occurrences

{% include  quote_occurence_7day_ma.html %}
{% include  accumulated_quotation_share_by_speaker.html %}
{% include  accumulated_quotation_count_by_occupations.html %}


3) Can we see the clusters of "meaning" depending on the occupation/age/year/gender.

- Plot a scatter of the embeddings (reduce dimensionality with PCA/UMAP/T-SNE) and color the dots by occution/gender/age

{% include  embeddings.html %}
