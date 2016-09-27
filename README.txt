In this project I have performed an automated sentiment analysis of customer reviews from the Yelp dataset. The goal is to analyze the review text and compute a sentiment score.  A high sentiment score would mean the review is positive and says good things about the business, and a low (negative) sentiment score would mean the review is negative and says bad things about the business. I then see how the sentiment score correlates with the average star rating. This was a part of the SI 618 home work. This contains two files along with the Yelp dataset and the text file containing word polarities

si618_hw4_part1_vedula.py: Run this file first to compute the average star rating ratings and the sentiment scores of the reviews of all the businesses in the dataset. This will take a while as the dataset is big.

si618_hw4_part.R : In this I perform the linear regression of sentiment score vs average rating. Run this second. 

The Pearson correlating coefficient between the average sentiment score and average star rating is in the file correlation.txt
