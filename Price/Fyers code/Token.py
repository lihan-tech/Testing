# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Define your Fyers API credentials
client_id = "D7D574OOFI-100"  # Replace with your client ID
secret_key = "07U9TIG1YP"  # Replace with your secret key
redirect_uri = "https://www.google.com/"  # Replace with your redirect URI
response_type = "code" 
grant_type = "authorization_code"  

# The authorization code received from Fyers after the user grants access
auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MjQ0OTg4NDAsImV4cCI6MTcyNDUyODg0MCwibmJmIjoxNzI0NDk4MjQwLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJZSDAwMzAyIiwib21zIjoiSzEiLCJoc21fa2V5IjoiZDg1OGE2OTQyNTJiN2UyZmM2MGM2ZTc0NWVhNzg3Mjc2YWI2OTc4OGExOGExYzY5MWVkMDU3ZGMiLCJub25jZSI6IiIsImFwcF9pZCI6IkQ3RDU3NE9PRkkiLCJ1dWlkIjoiOWM3YjVhMzE3ZmUzNDgyN2FhMDdhZDJmMWU2NzUxYmIiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.x9gC0trLKy-7T6bjGpKFnJKBRO8mypH4SLc1EqVl0kg"

# Create a session object to handle the Fyers API authentication and token generation
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key, 
    redirect_uri=redirect_uri, 
    response_type=response_type, 
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response = session.generate_token()

# Print the response, which should contain the access token and other details
print(response)

