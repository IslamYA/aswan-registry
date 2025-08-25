# Setup Rebar Material Script

This script generates a rebar material for use in Abaqus simulations.

## Usage

To use this script, simply run it and follow the prompts to input the required material properties.

### Input Parameters

* `density`: The density of the rebar material (tonne/mm^3)
* `E`: The Young's modulus of the rebar material (MPa)
* `poisson_ratio`: The Poisson's ratio of the rebar material
* `sigmaY`: The yield strength of the rebar material (MPa)
* `sigmaU`: The ultimate tensile strength of the rebar material (MPa)
* `fracStrainEng`: The engineering strain at fracture (elongation)
* `nPoints`: The number of interpolation points for the stress-strain curve
* `material_name`: The name of the material to be generated

## Output

The script generates a rebar material with the specified properties and saves it to the Abaqus model.

## Notes

* This script uses the `generate_stress_strain` function to generate the stress-strain curve for the rebar material.
* The `eng_to_true_stress` and `eng_to_true_strain` functions are used to convert engineering stress and strain to true stress and strain, respectively.

## Author

Dr. Nour