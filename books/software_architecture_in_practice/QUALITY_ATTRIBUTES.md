# Quality Attributes

* If the system requires **high performance**:
  * Need to pay attention to time based behavior of elements
  * Use of shared resources, frequency and volume of inter-element communication
* If **modifiability** is important:
  * Pay attention to assigning responsibilities
  * Ensure the majority of changes will affect a small number of elements
  * (Ideally one element lmao)
* If the system must be **highly secure**
  * Need to manage and protect inter-element communication
  * Control which elements are allowed to access which information
* If **scalability** is critical:
  * Need to localize the use of resources
  * This facilitates introduction of higher-capacity replacements
  * Avoid hard-coding resource assumptions or limits
* If the project needs to be able to deliver **incremental** subsets:
  * Need to carefully manage intercomponent usage
* If you want the elements to be **reusable** in other systems:
  * Need to restrict inter-element coupling
  * When you extract an element, it should not come out with many attachments
* If you care about **system availability**, you have to be concerned with:
  * How components take over for each other in the event of failure
  * How the system responds to fault
* If you care about **usability**
  * How to isolate details of the user interface
  * Allow those components to be tailored and improve over time
* If you care about **testability**
  * Need to be able to test individual elements
  * Have to make their state observable and controllable
  * Also need to understand the emergent behavior of elements working together
* If you care about **safety**
  * Must be concerned with behavioral envelope of the elements
  * Also how the elements work together in concert
* If you care about **interoperability**
  * Must be concerned with elements that are responsible for external interactions
  * Must be able to control these interactions
