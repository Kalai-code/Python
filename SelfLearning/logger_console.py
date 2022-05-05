import sys,logging

# STEP 1. Create a LOGGING Object
tiConsLog = logging.getLogger('kalai-console')

# STEP 2. Create a Streamhandler for the LOGGING Object
ConsHandler = logging.StreamHandler( sys.__stdout__ )

# STEP 3. Set Log Formatting
formatter = logging.Formatter('[%(asctime)s] %(name)-12s: %(levelname)-8s %(message)s')
ConsHandler.setFormatter(formatter)

# STEP 4. Add the Console Handler to the LOGGING Object
tiConsLog.addHandler(ConsHandler)

# STEP 5. Set Log Level
tiConsLog.setLevel(logging.DEBUG)
# print(tiConsLog.getEffectiveLevel())


# Use the functions [debug, info, warn, error] of the logging object
tiConsLog.debug('This is a debug message')
tiConsLog.info('This is a info message')
tiConsLog.warning('This is a warning message')
tiConsLog.error('This is an error message')
tiConsLog.critical('This is a critical message')

# Change Log level and retry logging all level log messages
tiConsLog.setLevel(logging.ERROR)

tiConsLog.debug('This is a debug message')
tiConsLog.info('This is a info message')
tiConsLog.warning('This is a warning message')
tiConsLog.error('This is an error message')
tiConsLog.critical('This is a critical message')