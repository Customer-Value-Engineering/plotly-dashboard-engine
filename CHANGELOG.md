# Change Log

All notable changes to this project will be documented here in the [Keep a
Changelog format](https://keepachangelog.com/en/1.0.0/). This project adheres to
[Semantic Versioning](http://semver.org/).

## v0.3.0 - 2021-06-03

### Added
  - Introduced VaexFileConnectionProvider

### Changed
  - Refactored `SelectionQuery`'s `select` and `group_by` to more closely match SQL semantics
  - Introduced `SelectionQueryResult`  to contain the result of queries and decouple `Connection` and `Element`

### Fixed
  - Fix "No data available" error when zooming too much in a scatter
  - Reordering of columns in a table
  
## v0.2.0 - 2021-05-05

### Added
  - x/y group-by on scatter, plus optional aggregated color and size
  - stacked vs grouped bar mode control
  - live/visually-lightweight editor required-field validation
  - legend control on scatter/bar/line elements
  - support for data columns with a "string" dtype
  - require `id` for `make_state_and_*`
  - instructions for running sample apps on Windows
  - Vaex connection

### Changed
  - Changed schema validation messages to be more informative
  - Changed the "cursor" icon into a more appropriate "tasks" icon
    and added a descriptive message for elements without types

### Removed
  - Removed the bug-prone "Copy text to clipboard" button on some docs examples
  - Remove element "New"

### Fixed
  - Fix problem with DateRangePicker element
  - Fixed a bug where docs and snapshot sample apps would not run on Windows
  - Changed an incorrect (static) README reference to sqlite `.db` files for sample app
    snapshots, and changed the sample app `.db` default to `'sqlite:///:memory:'`
  - Callback error when switching element's type using the editor
  - Indicator allows all numerical data types

## v0.1.0 - 2021-04-16

Initial release!
