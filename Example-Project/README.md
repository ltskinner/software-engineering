# Example-Project

```
/data
  /raw
  /enriched
/docs
  /requirements
  /architecture
  /design
  BACKLOG.md        --> use Issues + Projects
  RELEASE_NOTES.md  --> use Releases
/models
  model_weights.h5  --> consider grouping w2v, deep
/project
  /lib
    banner.txt
  /tests
    unittest + mock?
  /subpackage
    __init__.py
    submodule.py
  __init__.py
  module.py

setup.py
README.md
requirements.txt
tox.ini
```

## Naming Conventions

### Project

#### Overall-Project

* Capitalized-With-Hyphens
* OrNoSpaces
* Git-Repositories

#### code_package

* lowercase_underscores

#### modules.py

* lowercase_underscore

### Docs

* Word_Documents.docx, PDF_Docs.pdf, Visio.vsdx
  * Capitalized, '_'
* MARKDOWN.md, USE_CAPS_UNDERSCORES.md

### Data

* use_dates_YYYY_MM_DD.csv

### Models

* version_models_v1.h5
* use_dates_too_YYYY_MM_DD.h5
