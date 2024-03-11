from configparser import ConfigParser

config = ConfigParser()

config["app_settings"] = {
    "screenshot_filepath": "SCREENSHOT FOLDER GOES HERE",
    "api_key": "OPENAI API KEY GOES HERE"
}

with open("app_settings.ini", "w") as f:
    config.write(f)