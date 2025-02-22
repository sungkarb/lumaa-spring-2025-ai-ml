# Movie Recommendation System

A simple movie recommendation system that suggests movies based on user input using TF-IDF and cosine similarity.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Overview
This script searches through movie database to find matching titles from user prompt and infered genres

## Features
- Loads and preprocesses a movie dataset from a CSV file.
- Uses TF-IDF vectorization to analyze movie overviews.
- Infers genres from the prompt and integrates them into the recommendation process.
- Provides a ranked list of recommended movies.

## Prerequisites
Make sure to install latest version of Python before running the script

## Installation
Run following commands in the terminal to setup virtual environment and dependencies.
```
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
```

## Usage
To run the script, you need to specify your movie prompt in the terminal. Optioanlly,
you can choose how many top matched movie titles to show. By default, this parameter is
set to 5. 

## Example
Without the specifying number of matches
```
cd .src
python3 recommend.py "Recommend me good christmas movies to watch with family"
```
With specifying number of matches
```
cd .src
python3 recommend.py "Recommend me good christmas movies to watch with family" 10
```

## Video Demonstration
[![Watch the video](https://i.sstatic.net/Vp2cE.png)](https://youtu.be/Z7s42PrR3Rg)
