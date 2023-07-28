# Documentation: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/logging/lab-8
# Adding messages into your code that provide metadata info about how the code is executed is known as logging

# debug(msg, *args, **kwargs) - Logs a message with level DEBUG on the root logger.
# info(msg, *args, **kwargs) - Logs a message with level INFO on this logger. The arguments are interpreted as for debug().
# warning(msg, *args, **kwargs) - Logs a message with level WARNING on this logger. The arguments are interpreted as for debug().
# error(msg, *args, **kwargs) - Logs a message with level ERROR on this logger. The arguments are interpreted as for debug().
# critical(msg, *args, **kwargs) - Logs a message with level CRITICAL on this logger. The arguments are interpreted as for debug().
# log(level, msg, *args, **kwargs) - Logs a message with integer level level on this logger. The other arguments are interpreted as for debug().
# exception(msg, *args, **kwargs) - Logs a message with level ERROR on this logger. The arguments are interpreted as for debug(). Exception info is added to the logging message. This method should only be called from an exception handler.

# Import logging
import logging
import json

# This uses a json string as an input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

# Defines two variables to store the language code from the input.
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# The if statement checks to see if the language code is the same as the source code
if SourceLanguageCode == TargetLanguageCode:
    logging.warning("The SourceLanguageCode is the same as the TargetLanguageCode - stopping") # This will print to the console as the default level is warning
else:
    logging.info("The Source Language and Target Language codes are different - proceeding") # This will not print to the console because it is lower than warning
