# software-engineering

Notes on programming + best practices, design patterns, architectural patterns, and project management

* For actual implementations, see: [ltskinner/cicd](https://github.com/ltskinner/cicd)
* Includes:
  * 🏛️ Standard File Structure
  * 🐍 Python examples
    * [`setup.py`](https://github.com/ltskinner/cicd/blob/master/setup.py)
    * [`module.py` examples](https://github.com/ltskinner/cicd/blob/master/boneless/module.py)
    * subpackage examples
      * relative imports
      * [package `__init__.py` example](https://github.com/ltskinner/cicd/blob/master/boneless/__init__.py)
      * [subpackage `__init__.py` example](https://github.com/ltskinner/cicd/blob/master/boneless/subpackage/__init__.py)
      * [subpackage usage](https://github.com/ltskinner/cicd/blob/master/boneless/module.py)
    * [testing examples](https://github.com/ltskinner/cicd/tree/master/boneless/tests)
      * [executing tests](https://github.com/ltskinner/cicd#executing-tests)
    * [packaging example](https://github.com/ltskinner/cicd#bulding-package)
  * ⚙️ Config file examples
    * [.coveragerc](https://github.com/ltskinner/cicd/blob/master/.coveragerc)
    * [.gitignore](https://github.com/ltskinner/cicd/blob/master/.gitignore)
    * [MANIFEST.in](https://github.com/ltskinner/cicd/blob/master/MANIFEST.in)
    * [buildspec.yml](https://github.com/ltskinner/cicd/blob/master/buildspec.yml)
    * [logging.conf](https://github.com/ltskinner/cicd/blob/master/logging.conf)
    * [requirements.txt](https://github.com/ltskinner/cicd/blob/master/requirements.txt)
    * [tox.ini](https://github.com/ltskinner/cicd/blob/master/tox.ini)

## Quick Reference

| **Best Practices** | | |
| - | - | - |
| [Programming](./best_practices/PROGRAMMING.md) |  [Naming Conventions](./best_practices/NAMING_CONVENTIONS.md) | [Diagramming](./best_practices/DIGRAMMING.md) |
| | | |
| **Agile** | | |
| [Agile Rules](https://github.com/ltskinner/software-engineering/blob/master/books/agile_project_management_with_scrum/RULES.md) | [Sprint Planning](./checklists/SPRINT_PLANNING.md) | [Sprint Review](./checklists/SPRINT_REVIEW.md) |

## Step 1 - What

### Requirements

"Requirements are like water. They're easier to build on when they're frozen"

* [Code Complete Requirements](./books/code_complete/prereqs/requirements)
* [The Pragmatic Programmer Requirements](./books/pragmatic_programmer/CHAPTER_7.md)
* [Requirements **Peer Reviews**](./reviews/REQUIREMENTS.md)

### Software Estimating

## Step 2 - How

### Architecture

**Architecture is the design of constraints that apply system wide**

"When you look at the architecture, you should be pleased by how natural and easayy the solution seems."

* [Software Architecture in Practice](./books/software_architecture_in_practice)
* [Code Complete Architecture](./books/code_complete/prereqs/architecture)

### Design

**Design is the process of compartmentalizing the system into packages/subsystems, classes, and routines while keeping complexity to an absolute minimum**

"Once you understand that all other technical goals in software are secondary to managing complexity, many design considerations become straightforward"

* [Code Complete Design](./books/code_complete/design)
* [Design Patterns](./books/design_patterns)

## Step 3 - Implement

### Programming

* [Code Complete Programming](./books/code_complete/programming)
* [The Pragmatic Programmer](./books/pragmatic_programmer)

### Quality Assurance

"If builders built buildings the way programmers wrote programs, then the first woodpecker that came along would destroy civilization"

* [Code Complete Quality Assurance](./books/code_complete/quality_assurance)
* [Python Unit Test Example](./python/unit_testing)

#### [-> Peer Reviews](./quality_assurance/peer_reviews)

#### [-> Testing](./quality_assurance/testing)

### Software Metrics

* Agile Metrics

## Step 4 - Project Teardown + Debrief

### Maintenance

* [Code Complete Maintenance](./books/code_complete/maintenance)

### Administrative Project Teardown + Debrief
