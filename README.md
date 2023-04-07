# Music-Repository
client server application that acts as a Music Repository


Consider a client server application that acts as a Music Repository . The client will choose from three diffrent genres like rock , folk , pop . The client will place the request to a central server will be responsible for single genre . Once the request is processed that particular song should be downloaded to the client side . Implement this application  using the concept you have learned so far

Approach:

Approach of creating this Music Repository is basically handling various genres(rock,folk,pop) of music separately . For this we use a separate server for separate genres . 

The client will choose any genre of music provided by the main server . After choosing a genre the main server will fetch all available music in the requested genre server and provide it to the client . 

The client will request any available song from the provided list of music and the main server will download the requested 

