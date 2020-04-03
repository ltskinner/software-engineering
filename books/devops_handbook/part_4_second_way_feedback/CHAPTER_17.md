# Chapter 17: Integrate Hypothesis-Driven Deployment and A/B Testing into Our Daily Work

Before we build a feature, we should rigorously ask ourselves, "Should we build it, and why?"

* After deciding its worth building:
  * Perform the cheapest and fastest experiments possible to validate through user research whether the feature is wanted

## Integrating A/B Testing Into

### Feature Testing

* Website users are randomly selected to control either the "A" or the "B"
* Depending on how the two are used, the better one is selected

### Release

* Need production telemetry at all levels off the application stack
* Etsy had a good `Etsy A/N API` but is no longer supported :/

### Integrating into Feature Planning

* Use the Hypothesis Format:
  * We Believe: ...
  * Will Result: ...
  * We Will Have Confidence to Proceed When: ...
