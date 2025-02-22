# Movie Recommendation System

A simple movie recommendation system that suggests movies based on user input using TF-IDF and cosine similarity.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Overview
This script searches through movie database to find matching titles from user prompt and infered genres.

## Features
- Loads and preprocesses a movie dataset from a CSV file.
- Uses TF-IDF vectorization to analyze movie overviews.
- Infers genres from the prompt and integrates them into the recommendation process.
- Provides a ranked list of recommended movies.


https://github.com/user-attachments/assets/b2651b53-0285-4b78-b8e6-54d799aaff11

## Dataset
Dataset used for this project is "The Movies Dataset" by Rounak Banik 2018 [https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset]. This dataset is comed pre-installed and is located in 'data' folder.

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
First prompt produces titles ["Christmas Land", "Santa Paws 2: The Santa Pups", "Coming Home for Christmas", "Beverly Hills Chihuaha 2", "Pete's Christmas"] while second adds ["Double, Double, Toil, and Trouble", "Barbie in 'A Christmas Carol'", "Christmas Oranges", "Curious George: A Very Monkey Chirstmas", "Santa Claws"] to the list.

## Video Demonstration
https://github.com/user-attachments/assets/fbf17818-51dc-40ea-82e5-10204ee9c255
