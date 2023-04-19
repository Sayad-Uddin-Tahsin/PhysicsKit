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
- Built-in Unit Converter to Meter and KG
