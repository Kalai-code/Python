import sys, logging

# STEP 1. Create a LOGGING Object
tiFileLog = logging.getLogger('kalai-file')

# STEP 2. Create a Log File Handler, the log messages will be created in 
#         this file
LogFile = logging.FileHandler('C:\\Kalai\\Python\\SelfLearning\\pythonLog.py')

# STEP 3. Add the handler to the logging object
tiFileLog.addHandler(LogFile)

# STEP 4. Set Log Level
tiFileLog.setLevel(logging.ERROR)


# Run Log messages
tiFileLog.debug('This is a debug message')
tiFileLog.info('This is a info message')
tiFileLog.warning('This is a warning message')

# ONLY THE FOLLOEING MESSAGES ARE LOGGED TO FILE
tiFileLog.error('This is an error message')
tiFileLog.critical('This is a critical message')
