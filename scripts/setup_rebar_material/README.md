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

## Mathematical Theory

The script uses the following mathematical relationships to convert engineering stress-strain values to true stress-strain values for Abaqus plasticity modeling:

### Engineering to True Stress Conversion
$$\sigma_{\text{true}} = \sigma_{\text{eng}} \times (1 + \varepsilon_{\text{eng}})$$

Where:
- $\sigma_{\text{true}}$ = True stress
- $\sigma_{\text{eng}}$ = Engineering stress  
- $\varepsilon_{\text{eng}}$ = Engineering strain

### Engineering to True Strain Conversion
$$\varepsilon_{\text{true}} = \ln(1 + \varepsilon_{\text{eng}})$$

Where:
- $\varepsilon_{\text{true}}$ = True strain
- $\varepsilon_{\text{eng}}$ = Engineering strain

### Plastic Strain Calculation
For Abaqus plasticity definition, the plastic strain component is calculated as:
$$\varepsilon_{\text{plastic}} = \varepsilon_{\text{true}} - \frac{\sigma_{\text{true}}}{E}$$

Where:
- $\varepsilon_{\text{plastic}}$ = Plastic strain component
- $E$ = Young's modulus

### Stress-Strain Curve Generation
The script generates a piecewise linear stress-strain curve with the following points:

1. **Yield Point**: $(\sigma_y, 0.0)$ - where plastic strain begins
2. **Interpolated Points**: $n_{\text{Points}}$ evenly spaced points between yield and ultimate strength
3. **Ultimate Point**: $(\sigma_{\text{true},U}, \varepsilon_{\text{plastic},U})$ - calculated at fracture strain

The interpolation uses linear spacing in engineering stress domain:
$$\sigma_{\text{eng}}(i) = \sigma_Y + \frac{i}{n_{\text{Points}}} \times (\sigma_U - \sigma_Y)$$
$$\varepsilon_{\text{eng}}(i) = \frac{i}{n_{\text{Points}}} \times \varepsilon_{\text{fracture}}$$

## Output

The script generates a rebar material with the specified properties and saves it to the Abaqus model.

## Notes

* This script uses the `generate_stress_strain` function to generate the stress-strain curve for the rebar material.
* The `eng_to_true_stress` and `eng_to_true_strain` functions are used to convert engineering stress and strain to true stress and strain, respectively.
* Abaqus requires true stress and plastic strain values for plasticity definition.

## Author

Dr. Nour