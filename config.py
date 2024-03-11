from configparser import ConfigParser

config = ConfigParser()

config["app_settings"] = {
    "screenshot_filepath": "C:\\Users\\antho\\Documents\\wgushots",
    "api_key": "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"
}

with open("app_settings.ini", "w") as f:
    config.write(f)