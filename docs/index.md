# Hashing out the crypto talk

### "Words are chameleons, which reflect the color of their environment." —Learned Hand


What if from spoken words, we can analyze a new topic that somehow made a big impact on these last few years ? 
In this project we will try to analyse the subject of cryptocurrency from different angles using only the quotes provided by the QuoteBank dataset.  
### Why Cryptocurrency ?  
Cryptocurrency was the hottest investment story of the 2010s. Though for most of the 2000s, it didn’t exist. Now, it’s hard to get through a single week without a new digital currency making headlines. With Bitcoin now trading around $50,000 per coin, it is certainly here to stay.  Bitcoin was the original cryptocurrency, and it remains the most famous, most widely accepted one. However, there are many mysteries around the crypto world. The concept of Bitcoin was published in a white paper written by an anonymous figure under the pseudonym Satoshi Nakamoto in 2008. No one knows the author’s true identity — or if it’s even a single person, rather than a group of people. The mystery behind the creator of Bitcoin and the crypto world in general has captured our attention. With this project, we want to tackle most of the  questions surrounding cryptocurrency and answer them only by analyzing the QuoteBank dataset . When did it start, and from which group of people? How did it spread among the different groups (concerning occupations, genders, and age) over the years? Can we detect when its major events occurred?     
To answer these questions, we decided to study the story of cryptocurrency from 2008, the year of its creation up to 2017. Why up to 2017 only you might ask? In 2018, bitcoin became an international fever. Random companies were “pivoting to blockchain” creating a buzz. While it was a major year in the story of cryptocurrency, it put cryptocurrency in the spotlight and caused different persons among different groups to speak up. In order to analyze data that is coherent, we chose to cut the analysis in the year 2017.

### How did the crypto-popularity spread among the different occupation groups over the years?  

Let’s see the distribution over time of the occupation of the people that talked the most about blockchain and cryptocurrency.

{% include  quotes_by_occupation_slider_years.html %}  

As we can see, it started in 2008 with a specific group of people which are cryptographers , politicians , programmers , businesspersons , and scientists. We see these 5 groups speak up about cryptocurrency every year more or less. The first years until 2012 , programmers and politicians were taking the lead in the number of occurrences. Starting 2013 and until 2017, the businesspersons took the lead while the economists also started to speak up more starting 2014. 
In the year 2013, many lawyers spoke up about blockchain and cryptocurrency.It is an interesting observation since in that year bitcoin witnessed major developments in the legal framework and has received widespread attention from newspapers.  
In the years 2015 and 2016, the media group made its appearance among the top 5 occupations.  

#### Now let’s see how fast did the Bitcoin/Cryptocurrency hype spread inside those different professional groups.

{% include  accumulated_quotation_count_by_occupations.html %}

Here we can see that the rate was approximately the same until 2014, and after that businessmen started talking exponentially more… This quite makes sense, since in 2014 the whole world was discussing the event that we mentioned previously - the hack of the biggest crypto exchange. It is believed that there is no such thing as bad publicity, and that nicely plays with what we see here. Even thought the noticeable event was negative, it was an important starting point which drew attention of businesses to this technology, and after that - the topic spread faster and faster in the group.

We can also see that economists’ rate became much steeper in late 2016, since it was the time when bitcoin hit the unheard price of ~$20k. Economist started discussing how volatile it is, or how bitcoin will become the future of human economy. 

Below is shown the chart which shows the distribution of speakers' citizenship (taking into account the biggest parts). Just to make sure that the biggest part of the crypto party is hapenning in the United States.

We can se that the majority of the speakers are from the United States of America. We can also see that, other than the US, the distribution isn't very skewed towards one particular citizenship. This may imply that Bitcoin has became a worldwide topic.
{% include speakers_citizenship_pie.html %}

### Finding important events in the history of Bitcoin.

Let's take a look at the graph of quote occurrences over the years:

{% include  quote_occurence_7day_ma.html %}  

We can clearly see in this graph four major peaks: February 2014, September 2015, May 2016 and December 2017. This sudden increase in quotes lead us to the important events that happened in the crypto community:  
- February 2014: The world's largest bitcoin exchange, Mt. Gox, declared bankruptcy. The company stated that it had lost nearly $473 million of their customers' bitcoins. Mt. Gox blamed this on hackers who exploited transaction malleability problems in the network. This was equivalent to approximately 750,000 bitcoins, or about 7% of all the bitcoins in existence. The price of a bitcoin fell from a high of about $1,160 in December to under $400 in February.
- September 2015: Ledger, the first peer-reviewed academic journal dedicated to cryptocurrency and blockchain technology research was announced. It covers studies of cryptocurrencies and related technologies, and is published by the University of Pittsburgh. The journal encourages the use of digitally signed hashfiles, which will then be time stamped into the bitcoin blockchain.   
- May 2016: Multiple report were published alleging that the creator of bitcoin may be Craig Steven Wright, an Australian entrepreneur and former academic who has worked with K-Mart and the Australian Security Exchange. Then, on 2nd May, Wright publicly declared that he was, indeed, Nakamoto. This declaration created a big buzz in the cryptocurrency community given the position of Wright as one of the biggest figures in the domain.  
- December 2017: Bitcoin's price briefly reached a new all-time in December 17, nearing $20k, creating a massive reaction in the financial world. As a reaction to the ever growing price of bitcoin, the Software market Steam, announced that it would no longer accept bitcoin as payment for its products, citing slow transactions speeds, price volatility, and high fees for transactions.

### Distinguising true crypto guys, from those who joined the wave 

We’ve selected some of the noticeable figures in the history of bitcoin and visualized their "importance" in the global crypto-discussion. 

{% include  accumulated_quotation_share_by_speaker.html %}

Here on the Y axes we see the cumulative share of each speaker’s quotes relative to the general amount of the quotes about our selected topic.

For example if a person says something that goes viral ones, and then is not active, then we would see a decrease of his «importance in the world of Bitcoing discussion».

This is exactly what happened with Mark Karpeles for example. In 2014 his huge crypto exchange was hacked, and lost billions of dollars, and it was a very big deal, lots of noise and media attention. But after this  peak he became relatively less active in his public bitcoin-related discussion, and we notice that his «importance» slowly fades away on the plot above.

Simmilar thing can be said about Craig Wright. In 2016 he claimed to be Satoshi Nakomoto, which gave him some clout in the word of crypto, but made him somewhat of "anti-hero". We see that his wasn't any active before that claim, and after the controversial claim, his activity is slowly going down.

![This is an image](https://lh3.googleusercontent.com/a_SP8CsNOgyBNgha-PjVGM3tkt5aNl1847zODqCi0eEkPx7waKrqXONo-nAPo2ssXPH4DsMTmwxyGmOot5akQa6f8Rm8rzme4GjRs4etKGSE0yPXawEJYHww5iLlYBJEBS43-qNj)

On contrary, we see that Tyler Winklevoss is remaining constantly active, and same is true for a well-known Bitcoin advocate Andreas Antonopoulos. They remain on a constant level of relative activity, which means that when the World speaks more about bitcoin, their words spread more as well. 

This visualization also shows us when these people joined the public bitcoin discussion.
Craig wright started mid 2014, while Vitalik’s phrases were already noted in 2012.  


### Can we find the "different clusters of meaning" from the quotes about cryptocurrencies?

It would be nice if we could shortly answer the question: "What is all this crypto buzz about?". 

To find that answer we extracted "the meaning" of each quote by getting the embeddings of a language model, called "Sentence BERT". Now instead of reading every quote and trying to summarize it, we can project the "vectors of meaning" into the 2D space, and see whether we have clusters or not. Having a cluster would mean having a "general meaning" for all the quotes in that cluster. 

Below we can see the results. 

{% include  embeddings.html %}


We randomly set our algorithm to find 7 clusters, and it looks like we have a nice separation. We've selected some phrases from some of the clusters. 

#### Summary from cluster number 1: "Mainly boomer economists being mean to bitcoin"
>  "Who cares about bitcoin" - Jamie Dimon

> "Bitcoin remains a major gamble as it is very much an asset that remains in uncharted waters weve simply not experienced this before" - Jamie Dimon

> "Bitcoin in particular has had i think three hyperinflation episodes this year" - Paul Donovan

#### Summary from cluster 5: "Businessmen found a new way to become richer":
> "I have invested in some bitcoins myself and find it fascinating how a whole new global currency has been created" - Richard Branson

> "The legitimacy this gives bitcoin as a tradeable asset is very important" - Neil Wilson

> "I firmly believe that bitcoin and the blockchain can change the world for the better" - Craig Wright

#### Summary from cluster 6: "Cryptopeople cryptotalking":

> "My recommendation for people who dont have 10 years experience in cryptography is to return to old methods and use the traditional postal service" - Julian Assange

> "One unintended consequence of quantum computation is breaking some of the cryptographic tools currently underpinning cybersecurity" - Michele Mosca

> "Cryptography forms the basis for trust online" - Bruce Schneie

We see that it is possible to summarize the quotes, and group them by their meaning. This way we can group people by their opinion, and potentially find groups of people having the same opinion and spreading a simmilar message about the trendy topic.
