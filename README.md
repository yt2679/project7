# Squirrel Tracker: Django-Based Web Application For Tracking Central Park Squirrels

This is a Squirrel Tracker that used the open source data to establish a database of squirrels in Central Park and show them in the map.
User can add and update information about the squirrels sightings. 

## Group name

Project Group 7, Section 1

### UNIs

UNIs: [da2898, yt2679]

## Management commands

We provide two management commands:

* Import squirrel data:
  * Import a csv file to the database

* Export squirrel data:
  * Export squirrel data to the csv file

## Views

There are five views in the web app:

* Map
  * Located at: */map*
  * Shows the map of central park with squirrel sightings on it

* List Sightings
  * Located at: */sightings*
  * Shows the list of all  squirrel sightings

* Update Sightings
  * Located at: */sightings/unique-squirrel-id*
  * Edit the sightings of the squirrel of the unique squirrel id

* Add Sightings
  * Located at: */sightings/add*
  * Add new sightings 
  * Fields supported: Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, 
Location, Specific Location, Running, Chasing, Climbing, Eating, Foraging, Other Activities, Kuks, 
Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent, Runs from

* Sightings Stats
  * Located at: */sightings/stats*
  * Shows several stats about the squirrel sightings


