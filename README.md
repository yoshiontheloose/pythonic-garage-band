# Garage Band with OOP

**Author**: Clarissa
**Version**: 1.1.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for this class. (i.e. What's your problem domain?) -->

Creating a Garage Band with Object Oriented Programming.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Use Python classes to model a `Band` made up of different kinds of musicians.

Start with `Guitarist`,`Bassist`, and `Drummer`.

Make use of a `Musician` base class to handle common functionality which particular kinds of musicians will inherit.

*User Acceptance Tests*
Unit tests will be supplied for this lab. Your job is to make them pass. Do NOT modify the supplied tests (except to enable for stretch goals.)

**Band Tests**:

A `Band` instance should have a `name` attribute which is a string.

A `Band` instance should have a `members` attribute which is a list of instances that inherit from `Musician` base (or super) class.

A `Band` instance should have a `play_solos` method that asks each member musician to play a solo, in the order they were added to band.

A `Band` instance should have appropriate `__str__` and `__repr__` methods.

A `Band` should have a class method `to_list` which returns a list of previously created `Band` instances

**Musician Subclass Tests**:

Each kind of `Musician` instance should have appropriate `__str__` and `__repr__` methods.

Each kind of `Musician` instance should have a `get_instrument` method that returns string.

Each kind of `Musician` instance should have a `play_solo` method that returns string.

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Python, Poetry,

## Change Log
<!-- Use this area to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Application now has a fully-functional express server, with a GET route for the location resource. -->

## Estimates
<!-- See below -->
Estimate of time needed to complete:

Start time: 12/14

Finish time: 12/16

Actual time needed to complete: 6 hours

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->

Connor Boyce

Alex Payne

[str vs repr](https://www.geeksforgeeks.org/str-vs-repr-in-python/)

[python inheritance](https://www.w3schools.com/python/python_inheritance.asp)