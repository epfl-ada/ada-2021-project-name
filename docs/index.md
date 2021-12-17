## What's trending?

### "Words are chameleons, which reflect the color of their environment." —Learned Hand


What if from spoken words , we can analyze a new topic that somehow made a big impact on these last few years ? 
In this project we will try to analyse the subject of cryptocurrency from different angles using only the quotes provided by the QuoteBank dataset.
Why Cryptocurrency ?  
Cryptocurrency was the hottest investment story of the 2010s. Though for most of the 2000s, it didn’t exist. Now, it’s hard to get through a single week without a new digital currency making headlines. With Bitcoin now trading around $50,000 per coin, it is certainly here to stay.  Bitcoin was the original cryptocurrency, and it remains the most famous, most widely accepted one. However, there are many mysteries around the crypto world. The concept of Bitcoin was published in a white paper written by an anonymous figure under the pseudonym Satoshi Nakamoto in 2008. No one knows the author’s true identity — or if it’s even a single person, rather than a group of people. The mystery behind the creator of Bitcoin and the crypto world in general has captured our attention. With this project, we want to tackle most of the  questions surrounding cryptocurrency and answer them only by analyzing the QuoteBank dataset . When did it start, and from which group of people? How did it spread among the different groups (concerning occupations, genders, and age) over the years? Can we detect when its major events occurred?   
To answer these questions, we decided to study the story of cryptocurrency from 2008, the year of its creation up to 2017. Why up to 2017 only you might ask? In 2018, bitcoin became an international fever. Random companies were “pivoting to blockchain” creating a buzz. While it was a major year in the story of cryptocurrency, it put cryptocurrency in the spotlight and caused different persons among different groups to speak up. In order to analyze data that is coherent, we chose to cut the analysis in the year 2017.  
  
{% include  quotes_by_occupation_slider_years.html %}

2) When were the most «Popularity growing» events

- Show the graph with the shifted quote occurrences

{% include  quote_occurence_7day_ma.html %}

If we take a look at the graph of quote occurrences over the years, we can clearly see four major peaks: February 2014, September 2015, May 2016 and December 2017. This sudden increase in quotes can be traced to important events that happened in the crypto community:  
- February 2014: The world's largest bitcoin exchange, Mt. Gox, declared bankruptcy. The company stated that it had lost nearly $473 million of their customers' bitcoins likely due to theft, which Mt. Gox blamed on hackers who exploited transaction malleability problems in the network. This was equivalent to approximately 750,000 bitcoins, or about 7% of all the bitcoins in existence. The price of a bitcoin fell from a high of about $1,160 in December to under $400 in February.
- September 2015: Ledger, the first peer-reviewed academic journal dedicated to cryptocurrency and blockchain technology research was announced. It covers studies of cryptocurrencies and related technologies, and is published by the University of Pittsburgh. The journal encourages the use of digitally signed hashfiles, which will then be time stamped into the bitcoin blockchain.   
- May 2016: Multiple report were published alleging that the creator of bitcoin may be Craig Steven Wright, an Australian entrepreneur and former academic who has worked with K-Mart and the Australian Security Exchange. Then, on 2nd May, Wright publicly declared that he was, indeed, Nakamoto. This declaration created a big buzz in the cryptocurrency community given the position of Wright as one of the biggest figures in the domain.  
- December 2017: Bitcoin's price briefly reached a new all-time in December 17, nearing $20k, creating a massive reaction in the financial world. As a reaction to the ever growing price of bitcoin, the Software market Steam, announced that it would no longer accept bitcoin as payment for its products, citing slow transactions speeds, price volatility, and high fees for transactions.  

{% include  quote_occurence_change_by_date.html %}

- Take the couple of the events with the highest peaks and look more carefully into what happened there
- Show the graphs with time series segmentation

3) Can we see the clusters of "meaning" depending on the occupation/age/year/gender.

- Plot a scatter of the embeddings (reduce dimensionality with PCA/UMAP/T-SNE) and color the dots by occution/gender/age

