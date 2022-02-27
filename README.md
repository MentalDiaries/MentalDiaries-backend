# The backend for the codeutsav project MentalDiaries by Team AstuteForce.

This is a backend server for the project written in Django. 
It also runs a deeplearning model with natural language processing. The server has not been hosted anywhere as of now since free hostings were not able to host the entire deep learning libraries. 

The server hosts multiple end points for users login, registration, storage of data entries, etc.
In order to make the app more secure all the REST api operations use JWT authentication taking advantage of the public key cryptography features.
