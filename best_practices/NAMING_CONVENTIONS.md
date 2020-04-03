# Naming Convention Standards

## General

### Approved Abbreviations

* `col` for `column`
* `num` for `number` but **NEVER** `n`

## Dash Conventions

### className

* Template: `{id}_{spec}_{class}`

#### {id}

* **ONLY** elements that are the recipient of a callback
* Document elements as either
  * `{id}: {className}` if element has id
  * `{className}` if no id

#### {spec} options

If no {spec} is stated, assume its a combined set of elements

* `element`
* `dropdown`
* `radio`
* `slider`
* `navbar`

#### {class} options

* Element
  * `div`
* Positional
  * `row`
  * `col`
* Type
  * `title`
  * `text`

### Interactive Element Parameter Order

```python
dcc.Dropdown(
  id='{}_{}_{}',  # 1
  options=[],     # 2
  value=''        # 3
  # style={}  # NEVER style in Dash - ALWAYS use .css
)
```
