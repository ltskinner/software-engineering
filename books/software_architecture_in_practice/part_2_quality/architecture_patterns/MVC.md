# Model-View-Controller Pattern

## Overview/Elements

* MVC breaks system functionality into the three components
* Model: Contains the applications data
* View: Displays some portion of the underlying data and interacts with the user
* Controller: Mediates between the model and the view and manages the notifications of state changes

## Relations

* The *notifies* relation connects instances of model, view and controller, notifying elements of relavent state changes

## Constraints

* There must be at least one isntance of each model, view, and controller
* The model components should not interact directly with the controller

## Weaknesses

* Complexity may not be worth it for simple user interfaces
* The model, view, and controller abstractions may not be good fits for some user interface toolkits
