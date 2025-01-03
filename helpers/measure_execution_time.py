from datetime import datetime
from functools import wraps
from time import perf_counter
from typing import Any, Callable


def measure_execution_time(
	log_to_file: bool = False,
	log_file: str = "execution_times.log",
	decimal_places: int = 8,
	include_args: bool = False,
) -> Callable:
	"""
	A flexible decorator that measures and logs function execution time.

	Args:
		log_to_file (bool): If True, logs execution times to a file
		log_file (str): Path to the log file (used if log_to_file is True)
		decimal_places (int): Number of decimal places for time measurement
		include_args (bool): If True, includes function arguments in the log

	Returns:
		Callable: The wrapped function with timing functionality

	Example:
		@measure_execution_time(log_to_file=True, include_args=True)
		def my_function(x, y):
			return x + y
	"""

	def decorator(func: Callable) -> Callable:
		@wraps(func)  # Preserves the decorated function's metadata
		def wrapper(*args: Any, **kwargs: Any) -> Any:
			# Record start time
			start_time = perf_counter()

			try:
				# Execute the function
				result = func(*args, **kwargs)
				success = True
			except Exception as e:
				success = False
				exception_info = str(e)
				raise  # Re-raise the exception after logging
			finally:
				# Calculate execution time
				end_time = perf_counter()
				execution_time = end_time - start_time

				# Prepare log message
				timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
				log_message = (
					f"[{timestamp}] {func.__name__} " f"function took {execution_time:.{decimal_places}f} seconds"
				)

				# Add args and kwargs if requested
				if include_args:
					args_str = ", ".join([repr(arg) for arg in args])
					kwargs_str = ", ".join([f"{k}={repr(v)}" for k, v in kwargs.items()])
					params = ", ".join(filter(None, [args_str, kwargs_str]))
					log_message += f" | Args: ({params})"

				# Add status
				log_message += f" | Status: {'Success' if success else 'Failed'}"
				if not success:
					log_message += f" | Error: {exception_info}"

				# Console output
				print(log_message)

				# File logging if enabled
				if log_to_file:
					try:
						with open(log_file, "a") as f:
							f.write(log_message + "\n")
					except IOError as e:
						print(f"Warning: Could not write to log file: {e}")

			return result

		return wrapper

	return decorator
