import glob
import os
import pandas as pd
import requests
import json

# Folder where the CSVs are saved
folder_path = "D:/"

# Match any "packages*.csv" file
files = glob.glob(os.path.join(folder_path, "packages*.csv"))

# Get the most recently modified file
latest_file = max(files, key=os.path.getmtime)

# Load the latest CSV
df = pd.read_csv(latest_file)

# Group by RouteCode and TransporterName
summary = df.groupby(['RouteCode', 'TransporterName']).size().reset_index(name='Reattempts')

# Convert the summary to a message format
summary_message = summary.to_string(index=False)

# Chime Webhook URL
chime_webhook_url = 'https://hooks.chime.aws/incomingwebhooks/6023c1cd-6c82-4d28-a6d0-581e4cc2d751?token=anE0VkpZYVN8MXxfQXBQT05SMnJPbXpCeXlvRVI5Y3RFS0JGUGxKSGpTZ3kzY2ZoSmZWWkJz'  # Replace with your actual Chime Webhook URL

# Create the payload for Chime message
payload = {
    "Content": f"Using file: {latest_file}\n\nSummary:\n{summary_message}"
}

# Send the message to Chime
response = requests.post(
    chime_webhook_url,
    data=json.dumps(payload),
    headers={"Content-Type": "application/json"}
)

# Check if the request was successful
if response.status_code == 200:
    print(f"Message successfully sent to Chime with file: {latest_file}")
else:
    print(f"Failed to send message to Chime: {response.status_code}")
