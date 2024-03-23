# practice-sphinx
This repository will be used to practice documentation with Sphinx along with GH Workflows.

Link to the [Official Documentation](https://ca20110820.github.io/practice-sphinx/).

## References
- [A “How to” Guide for Sphinx + ReadTheDocs](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/index.html)
- [John Robertson's Example](https://github.com/Robbozinoz/tic_tac_toe_docs/tree/main)
- [How to document your research software](https://coderefinery.github.io/documentation/)
  - Specifically the commands from [this](https://coderefinery.github.io/documentation/sphinx/) page.

## Notes
I modified some scripts tailored to match the project file structure pattern described below.:
```text
.
├── docs/
│   ├── _build/
│   ├── source/
│   │   ├── _static/
│   │   ├── _templates/
│   │   ├── index.rst
│   │   ├── conf.py
│   │   └── *.rst
│   ├── make.bat
│   └── Makefile
├── src/
│   └── some_package/
│       ├── __init__.py
│       └── *.py
└── tests/
    └── test_***.py
```
