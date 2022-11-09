# GS Live

TODO: Description

# Usage

```GS.py```

Launches the Ground Station service selector. 

# Services

These services are available/planned:

- Scheme editor
  - Allows you to create, copy, edit, and delete schemes.
  - *Not yet implemented*
- Animator
  - Creates an live animation of the vehicle in flight.
  - *Not yet implemented*
- Logger
  - Creates a data logging service.
  - *Not yet implemented*
- DAC translator
  - Creates a service to translate analog data to digital binary data.
  - *Not yet implemented*
- Socket server
  - Creates a service which all other services connect to.
  - Used to manage the entire ground station.
  - Must be started before any clients can be properly configured.
  - *Not yet implemented*
- Listener client
  - Creates a custom socket listener client.
  - Used to add additional functionality.
  - *Not yet implemented*
- Processor client
  - Creates a processor socket client.
  - Used to process data to pass back to the socket server.
  - *Not yet implemented*

# Schemes

Schemes are profiles used for individual vehicles. They contain all necessary information to understand the vehicle's data.

TODO: List and explain every attribute of a scheme
