# Parking lot

https://github.com/ashishps1/awesome-low-level-design/blob/main/problems/logging-framework.md

## Requirements

1. The logging framework should support different log levels, such as DEBUG, INFO, WARNING, ERROR, and FATAL.
2. It should allow logging messages with a timestamp, log level, and message content.
3. The framework should support multiple output destinations, such as console, file, and database.
4. It should provide a configuration mechanism to set the log level and output destination.
5. The logging framework should be thread-safe to handle concurrent logging from multiple threads.
6. It should be extensible to accommodate new log levels and output destinations in the future.

## Things to remember

1. Add a `get_instance` method to Singleton classes. That way you can get the instance from everywhere with
`Logger.get_instance()` instead of passing the instance variable around.
2. How to implement ordering for `Enum`s.
3. User functions should be simple and pass as little varibles as necessary: `logger.info(message)` vs `logger.log(dt, LogLevel.INFO, message)`