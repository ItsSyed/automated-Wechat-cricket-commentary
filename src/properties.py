# Non-MacOS users can change it to Chrome/Firefox.
BROWSER = "Chrome" # can be Chrome/Safari/Firefox
MATCH_URL = "https://www.espncricinfo.com/series/19245/commentary/1201941/south-africa-women-vs-sri-lanka-women-sl-w-in-australia-2019-20"
MESSAGE_BOX_CLASS_NAME = "content"
SEND_BUTTON_CLASS_NAME = "action"

# Match start timings according to where the script is being run.
MATCH_START_HOURS = 8
MATCH_START_MINUTES = 43
MATCH_END_HOURS = 23
MATCH_END_MINUTES = 0
SCRIPT_LOG_FILE_NAME = '../logs/script_logs.log'
ERROR_LOG_FILE_NAME = '../logs/error_logs.log'

# This tells whether the script is running in test mode or not. If yes, the actual data sent is less, for better debugging.
IS_TEST_MODE = False
