## [1.4.0]
### Added
- Accessibility improvements (colour-independent state cues, contrast, font).

## [1.3.1]
### Fixed
- Out-of-domain input no longer crashes (NFR-4); corrected exception chaining.
### Added
- Unit tests for input parsing: FR-1 (valid number), FR-5 (out-of-domain),
  FR-6 (non-numeric).

## [1.3.0]
### Changed
- Refactored GUI logic into testable functions; importability guard.
### Added
- PyUnit suite covering FR-1, FR-5, FR-6, FR-10, FR-11, NFR-2.

## [1.2.0]
### Fixed
- Accuracy for negative inputs (FR-1, NFR-2), verified to 3 decimals.
### Added
- Maximum-iteration cap with ConvergenceError (new D3 reliability requirement;
  supports NFR-1 timing and NFR-4 stability).

## [1.1.0]
### Added
- Clear button (FR-9, continuous computation) and Exit button (FR-7).

## [1.0.0] - D2 baseline  
- From-scratch arccos(x), GUI, validation, radians + degrees to 3 decimals.