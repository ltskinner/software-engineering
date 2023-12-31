# Chapter 10. Recommendations in Development

The netflix prize was an open ml competition aimed to build an algorithm capable of besting netflixs own content rating prediction process

One specific derivative of the prize sent waves thru the graph theory community. it ignited the use of graph thinking as a solution fro traditionally matrix-based algorithms

The realizaiton was that it is much easier to explain recco systems with a graph than with a matrix recco

The comp popularized the idea of using relationships between users and movies to predict and personalize your digital experience

## Recommendation System Examples

### Healthcare

### Social Media

### Ecommerce

## An Introduction to Collaborative Filtering

Collaborative filtering with graph structures is proven technique for personalizing content reccs

- Collaborative filtering: Type of rec system that predicts new content (filtering) by matching the interests of the individual user with the preferences of many users (collaborating)

### Understanding the Problem and Domain

- Content-based rec systems are focused only on the preferences of the user

### Collaborative Filtering with Graph Data

- User-based collaborative filtering: Finds similar users who share the same rating patterns as the active uer to rec new content
- Item-based collaborative filtering: Finds similar items according to how users rated those items to rec new content

### Recommendations via Item-Based Collaborative Filtering with Graph Data

### Three Different Models for Ranking Recommendations

- Path counting: think literally just counting number of paths to reach
- Net Promoter Score-inspired metric: popular metric that uses a scale to quantify how likely someone is to rec to a friend
- Normalized Net Promoter Scores: sameas just normalized by degree

## Movie Data: Schema, Loading, and Query Review

### Data Model for Movie Recs

### Neighborhood Queries in the Movie Data

### Tree Queries in the Movie Data

### Path Queries in the Movie Data

## Item-Based Collaborative Filtering in Gremlin
