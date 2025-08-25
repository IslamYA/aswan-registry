from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# Get the first model in the mdb
model = mdb.models.values()[0]

# Create material
material_name = "STEEL_sun_y415_u580_e145_n4"
model.Material(name=material_name)
material = model.materials[material_name]

# Set material description
material.setValues(
    description="Steel material: yield=415 MPa, ultimate=580 MPa, E=204 GPa, density=7.8e-09 tonne/mm^3."
)

# Define elastic properties
material.Elastic(
    dependencies=0,
    moduli=LONG_TERM,
    noCompression=OFF,
    noTension=OFF,
    table=((204000.0, 0.3),),
    temperatureDependency=OFF,
    type=ISOTROPIC,
)

# Define density
material.Density(
    dependencies=0,
    distributionType=UNIFORM,
    fieldName="",
    table=((7.8e-09,),),
    temperatureDependency=OFF,
)

# Define plastic properties
material.Plastic(
    dataType=HALF_CYCLE,
    dependencies=0,
    hardening=ISOTROPIC,
    numBackstresses=1,
    rate=OFF,
    strainRangeDependency=OFF,
    table=(
        (415.0, 0.0),
        (472.789062, 0.03329083),
        (533.56875, 0.06737684),
        (597.339062, 0.10030512),
        (664.1, 0.13214924),
    ),
    temperatureDependency=OFF,
)

# Set material identifier
material.setValues(materialIdentifier="")
