# Py-CAN-Module
A patch for python Module - CAN

## Goal
Build Python module on a raspberry Pi to emulate different hardware as CAN nodes. The module should send and recieve messages with the car's central control unit behaving like the replaced hardware. This allows the electrical team to individually test hardware outside of the car which is much more efficent and accessible.

## Requirements
Produce a python module for CAN messages.
- Tx and Rx functions for transmitting and receiving messages.
- Logging functionality to record message id, data sent/received and the time at which it took place.
- Functions for running specific CAN messages.
