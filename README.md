# PhysicsKit

`PhysicsKit` is a Python library that provides a set of tools for performing physics calculations. With `PhysicsKit`, you can easily calculate the force, velocity etc, making it a powerful tool for working with physics data.

```py
import physics

mass1 = 10  # kg
mass2 = 5  # kg
distance = 2  # meters
force = physics.gravity.Gforce(mass1, mass2, distance)

print(f"The force between the objects is {force} Newtons.")
```

## Installation

Currently, PhysicsKit is not available on PyPI as it is still under development. However, you can install it directly from the repository using the following command:
```console
pip install git+https://github.com/Sayad-Uddin-Tahsin/PhysicsKit.git
```

## Supported Calculations:

- Gravity
  - Gravitational Force between two objects (`Gforce`)
  - Distance between two objects (`distance`)
  - Mass of first object (`m1`)
  - Mass of second object (`m2`)
  - Weight of an object (`weight`)
  - Velocity of an object (`velocity`)
  - Displacement of an object (`displacement`)
  - Time required to travel a distance at a given velocity (`time_required`)
  - Acceleration of an object (`acceleration`)
  - Time taken to reach a certain velocity (`time_to_reach_velocity`)
  <details>
  
  <summary>Show More</summary>
  
  - Force exerted on an object based on its mass and acceleration (`force`)
  - The amount of energy an object possesses due to its position (`gravitational_potential_energy_at_height`)
  - The gravitational potential energy between two objects (`gravitational_energy_between_two_masses`)
  - Escape Velocity (`escape_velocity`)
  - The period of an object in circular orbit (`period_of_orbit`)
  - The orbital velocity of an object in circular orbit (`orbital_velocity`)
  - The gravitational potential energy (`gravitational_potential`)
  - The gravitational field strength (`gravitational_field_strength`)
  - The gravitational acceleration (`gravitational_acceleration`)
  - The gravitational time dilation (`gravitational_time_dilation`)
  - The Schwarzschild radius (`schwarzschild_radius`)
  - The gravitational redshift (`gravitational_redshift`)
  - The Chandrasekhar limit for a given value of xi (`chandrasekhar_limit`)
  - The Roche limit (`roche_limit`)
  - The radius of a geostationary orbit (`geostationary_orbit`)
  
  </details>
- Built-in Unit Converter to Meter and KG
