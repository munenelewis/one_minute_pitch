# one minute pitch

 This web app is a place where users can come in regester and post there pitches for other people to read and comment ...

## By **[Lewis munene](https://github.com/munenelewis)**

## Description
[This]  is a web application that users can add any category they want and post it so that other users can see there ideas and also vote and comment accodding to there thoughts

## User Stories
As a user I would like:
* to add different category
* to comment on other people post
* to like and dislike pitches
* to add comments anytime

## Specifications
| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Display all categories | category name| category is added and piches can be added to it |
| like and dislike pitches| **Click** the like or dislike button|
| Display all comment, date and time posted | N/A | all comments are outputed and date they were posted |

## Prerequisites
* Python3.6

## How to use it
* must have internet connection
* Click https://lewne.herokuapp.com/) <br/>
  or <br/>
* Copy https://lewne.herokuapp.com/ ) and  Paste the link on your prefered browser


## Setup/Installation Requirements
* internet access
* git clone https://github.com/munenelewis/one-minute-pitch
* $ cd one-minute-pitch
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh

# CREDITS

#### Google.com, StackOverflow.com and Miguel Grinberg -author of 'Flask Web Development'


# Support and Contacts

In case You have any issues using this code please do no hesitate to get in touch with me through munenelewis@gmail.com or leave a commit here on github.

## Known Bugs

No known bugs

## Technologies Used
- Python3.6
- Flask framework
- Bootstrap

### License

**[MIT](./LICENSE)** (c) 2017 **[Lewis munene](https://munenelewis.github.io)**