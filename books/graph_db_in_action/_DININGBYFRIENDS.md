# DININGBYFRIENDS

## Requirements

### 1. Social Network

Users want to connect with friends who are also using the application. Functionality is similar to the way users connect with friends on any social network like Twitter, LinkedIn or Facebook

### 2. Resuraount Recommendations

Uers want to create and look at reviews of resturaunts and then get recommendations for a resuraunt based on these reviews (the central service of the app)

### 3. Personalization

Users want to rate the reviews of resturaunts to indicate whether the review was helpful or not. Then they want to combine these reviews with their friends ratings to receive personalized recs

## What types of information does the application need to record to perform these tasks?

- Basic identifying information (name, ids)
- Resturaunt id and details, name, address, cuisine
- Text of the review, with rating and timestamp
- Reviews need to include ratings of its helpfulness (up/down arrows)

## Who are the users of our application?

## What questions does DBF need to answer for the User?

- Who are my friends
- Who are the friends of my friends
- How is user X associatedw tih user Y
- what resuraunt near me with a specific cuisine is the highest rated
- which resturaounts are the ten highest rated resturaunts near me
- what are the newest reviews for the rest
- what rest do my friends recommend
- based on my friends review ratings, what are the best restaruants for me
- what rest have my friends reviewed or rated in the past X days

## Entites

- Restaurant (includes name and location)
- Cuisine
- Person (first and last name)
- Review (text reivew and rating)

## Relations

remember - these are between entities we just defined only

if create relation that does not include above entity, likely need new entity, or relation is not as important lol

- person-friends-persin
- person-writes-review
- reviews-are about-resuraunt
- rest-serves-cuisine
- person-rates-reviews
