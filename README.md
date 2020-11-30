# YAML Hierarchical Search

## Synopsis

Quick and easy hierarchical utility to parse YAML/JSON in a tree search, or simply validate inputs

## To use these examples

### Ideal Usage

`| yhs`

### Actual Usage

`yhs.py example.yml`
`yhs.py "yaml"`

## Goals

- Quick and dirty YAML Structure Validation
- Accept either file handles or a string
- Accept as a pipe
- Search top level tree members for a string, then return the tree below it
- Search a provided depth tree members for a stirng, then return the tree below it
- Search arbitrary depths for a string, then return the tree below it

## Testing

TBD

### Dependencies

- Python 3
- `python3-ruamel.yaml`

## TODO

- Moved to project board

## Authors

- *Nick Schmidt*
