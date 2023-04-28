# Chapter 10. ML Interoperability

ONNX is pog

## Why Interoperability is Critical

## ONNX: Open Neural Network Exchange

### ONNX Model Zoo

### Convert PyTorch into ONNX

### Create a Generic ONNX Checker

### Convert TensorFlow into ONNX

### Deploy ONNX to Azure

## Apple Core ML

## Edge Integration

## Exercises

- [ ] Update all scripts to verify the produced ONNX model with the script from the chapter
- [ ] Modify the CoreML converter script to use the Click framework for better parsing of options and a help menu
- [ ] Group three converters into a single command line tool so that it is easy to make conversions with different inputs
- [ ] Improve the tf2onnx converter so that it is wrapped in a new script, which can catch common errors and report them with a more user-friendly message
- [ ] Use a different ONNX model for an Azure deployment

## Critical Thinking Discussion Questions

- Why is ONNX important? Give at least three reasons
- What is something useful about creating a script without a command line tool framework? What are the advantages of using a framework?
- How is the ORT format useful? In what situations can you use it?
- What are some problems that you may encounter if portability doesnt exist? Give three reasons why improving those problems will improve ML in general
