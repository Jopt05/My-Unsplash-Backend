## My Unsplash Backend

Project made on Django for [DevChallenges](https://devchallenges.io/challenges/rYyhwJAxMfES5jNQ9YsP)

## Set Up

Set up a virtual enviroment

    py -m venv virtual_env_name

Activate the enviroment and clone the repo.
Install requirements

    pip install -r requirements.txt

Apply migrations and run the server.

## Routes

**GET**

    /api/images

Get all images

**GET**

    /api/images/pk

Get all images from user

**POST**

    /api/images/post

Post a new image _(Requires token)_

    {
        "label":  "Omg master chief",
        "url":  "https://media.gq.com.mx/photos/61f99491247e703ee62fca75/16:9/w_2560%2Cc_limit/halo.jpg",
        "author":  "1"
    }

**POST**

    /api/login

Login an user

    {
    "username":  "james@hotmail.com",
    "password":  "12345678"
    }

**POST**

    /api/register

Register a new user

    {
    "name":  "Anais Hernandez",
    "email":  "ann30_hdz@outlook.es",
    "password":  "123456",
    "password2":  "123456"
    }

**DELETE**

    /api/images/delete/pk

Delete an image. _(Requires token and user password)_

     {
    "password":  "G5u50m4R05"
    }
