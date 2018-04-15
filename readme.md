# Hotel Manager

This program uses sqlite to build a database of hotel reservations and hotel settings (how many rooms and an overbooking level). This program uses the django rest api framework creating three endpoints.

^hotels/

Which shows a historical list of each time the hotels settings have been changed. We can also create a new hotel object using this endpoint.

^reservations/

Which shows all the current reservations as well as creating a new reservation.


^hotel_edit/<id>

This endpoint allows us to input a specific hotel object id and then allow us to modify it. (NOTE: this was an extra endpoint I created both for fun and thought it would be useful).



# Tests

I've created two unittests for test some of the calculations I was doing as well as verifying the reservation system would raise an error if we reached out maximum number of rooms we can book.

To run the tests on the commandline follow these steps :

1) in the folder where the repo is cloned, activate the virtual environment.

    source env/bin/activate

All the necessary modules and libraries are in the 'env' folder.

2) Activate the django run server:

    cd overbooked
    python manage.py runserver

3) In a separate shell :

    cd overbooked
    python manage.py test


This should run both unittests.


Furthermore each endpoint has a APIView, and can be interacted through the browser.

If you have any questions please send me an email at : michael.kambli@gmail.com