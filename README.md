# Sasquatch as a Service

This repository contains the code needed to build and deploy the microservice for the [Bigfoot Classinator](https://github.com/bigfoot-classinator). The irony of having a microservice for a macro-footed creature is not lost of me. Nevertheless, here were are.

The Bigfoot Classinator microservice, or, as I like to call it, _Sasquatch as a Service_ (SaaS), makes use of a model built with [DataRobot](https://www.datarobot.com/). The code and data for building that model can be found [here](https://github.com/bigfoot-classinator/bigfoot-classinator-model).

This README contains the instructions on how to use said code so that you can build the Bigfoot Classinator yourself. I expect this will make your weekly squatch hunts more productive.

## Build You a Model

This example uses a model built using [DataRobot](https://www.datarobot.com/). You'll need a model there before this code can work. Fortunately, there's a [repository](https://github.com/bigfoot-classinator/bigfoot-classinator-model) just for that purpose complete with all the code, data, and instruction you need. If you haven't already, go there and build a model.

> **NOTE**: When you're done building your model, you should have two environment variables set: DATAROBOTAI_API_KEY, and BIGFOOT_CLASSINATOR_PROJECT_ID. You'll need these set for the microservice as well.

## Install You a Python

You need a Python environment to make this all work. I used Python 3.7—the latest, greatest, and most updatest at the time of this writing. I also used `venv` to manage my environment.

I'll assume you can download and install Python 3.7 on your own. So lets go ahead and setup the environment.

    $ python3.7 -m venv venv

Once `venv` is installed, you need to activate it.

    $ . venv/bin/activate

Now when you run `python` from the command line, it will always point to Python3.7 and any libraries you install will only be for this specific environment.

If you want to deactivate this environment, you can do so from anywhere with the following command.

    $ deactivate

## Fetch You Some Dependencies

Now, it's time to install all the dependencies. These are all listed in `requirements.txt` and can be installed with `pip` like this.

    $ pip install -r requirements.txt

Run that command, and you'll have all the dependencies installed and will be ready to run the code.

## Start You a Server

So, all your ducks are in a row. Let's actually run this thing! Simple as simple can be.

    $ python app.py

You should see the following.

    * Serving Flask app "app" (lazy loading)
    * Environment: production
      WARNING: Do not use the development server in a production environment.
      Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

I note the warning. I ignore the warning. It's an old habit from C++ development in the 90s. The important thing is that our service is listening on port 5000. Let's try to hit it!

    **NOTE**: I'm going to use `curl` to do this since it's friendlier for the documentation. But, I'd recommend using [Postman](https://www.getpostman.com/) instead. It's like `curl`, but made for humans.

There are two endpoints on the service. The first one, a GET, just returns some basic information about the service. The name, an attribution saying we it uses DataRobot, and a version. This is a great one to hit to just make sure the services is up and callable since it just returns hard-coded results.

The other endpoint performs the classination for Bigfoot sightings. We'll talk more about it later. For now, let's just get some info on our service.

    $ curl http://127.0.0.1:5000/info

This will return a simple JSON string.

    {"app":"Bigfoot Classinator","attribution":"AI by DataRobot","version":"3.0.0"}

Hooray! It works.

## Classinate You a Bigfoot Sighting

So now we're ready to classinate some sighting with our microservice. We'll use the classination endpoint for this, which is a POST. As a POST, it is expecting some sort of body. In this case it is, as is so often the case, a JSON body.

Our JSON body is pretty simple. It has one field, the sighting. It looks something like this.

```json
{
  "sighting" : "I saw Bigfoot in the woods."
}
```

You're welcome to customize it with your own sightings like:

> "I saw Bigfoot out by the woodshed. He was 12 feet tall and covered in hair. I didn’t like the cut of his jib."

> "My dog heard a weird sound in the woods. The next day, we found a large footprint by the creek."

> "My grandfather used to tell me about the time he saw Bigfoot back in the 30s. He was walking along Moonville Road when he heard a large crash."

We're just gonna use a short one so that the `curl` command is easier to type.

    $ curl --request POST \
           --header "Content-Type: application/json" \
           --data '{"sighting": "I saw Bigfoot"}' \
           http://127.0.0.1:5000/classinate

```json
{
  "classination": {
    "class_a" : 0.6395407644,
    "class_b" : 0.3559792017,
    "class_c" : 0.0044800339,
    "selected" : "Class A"
  },
  "sighting" : "I saw Bigfoot"
}
```

Of course, it won't be that pretty. It'll be all squished up like this.

    {"classination":{"class_a" : 0.6395407644,"class_b" : 0.3559792017,"class_c" : 0.0044800339,"selected":"Class A"},"sighting":"I saw Bigfoot"}

## That's All Folks

That's it for this part of the Bigfoot Classinator. Check out some of the [other repositories](https://github.com/bigfoot-classinator) to see how to build
[three](https://github.com/bigfoot-classinator/bigfoot-classinator.github.io)
[different](https://github.com/bigfoot-classinator/bigfoot-classinator-client-ios)
[applications](https://github.com/bigfoot-classinator/bigfoot-classinator-client-console)
that use this service.
