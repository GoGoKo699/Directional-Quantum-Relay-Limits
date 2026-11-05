# Verification route

The authoritative commands, tested conventions, expected outputs and limits of the checks are in [REPRODUCIBILITY](../REPRODUCIBILITY.md). The finite calculations require the packages in [requirements.txt](requirements.txt).

The checked analytical argument is organized by topic under [science/](../science/README.md). The numerical record in [data/verification.json](../data/verification.json) checks finite realizations and formulas independently; it is not a numerical proof of an optimization over every passive chain.

There is no required hosted CI workflow in this repository. Run the documented local scientific checks when changing a formula, construction or numerical implementation. Regenerate the figures and their data when their inputs or evaluation code change.
