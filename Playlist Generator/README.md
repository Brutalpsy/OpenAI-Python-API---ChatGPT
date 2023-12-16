To run this app you would need to sign up for a Spotify developer account and 
create an app and get client id and client secret and also openai api key and put those things in a  <b>.env </b> file 
which content that should look like this:

SPOTIFY_CLIENT_ID=

SPOTIFY_CLIENT_SECRET=

OPENAI_API_KEY=

And after that it can be used with something like: 

<b> python app.py -p "best synthwave songs" -n 22 </b>
