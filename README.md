# Baloto lucky number to obtained

# About

This is code for scraping the lottery numbers uses historical lottery numbers from https://www.loterias.com/. The result lucky number obtained was just for fun. If you test this code, you should not use this number to play, as the most common numbers do not increases your chances of winning the lottery significantly.

# How data is collected

## Part 1: Getting a collection of all the games played

All data was scraped using the data from https://www.loterias.com/, specifically https://www.loterias.com/baloto/resultados which contains the data from the baloto, the biggest lottery in colombia.

## Part 2: Proceesing the data

With our collection of the games played, we need to create two dictionaries of games separetaly as baloto has two types of games. Revancha and normal.

1. First, we collect the data until 2017 as only normal, due to revancha being created this year
2. On 2017, we need to capture the special dates when revancha did not exist, to avoid data repetition in normal games
3. After the start of revancha is defined. We capture all the data, convert it to a dataframe and found the most common numbers for both games
