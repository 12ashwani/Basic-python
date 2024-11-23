import logging

# Logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

# Custom logger
logger = logging.getLogger("ArithmeticApp")

def add(a, b):
    result = a + b
    logger.debug(f'Adding {a} + {b} = {result}')
    return result

def sub(a, b):
    result = a - b
    logger.debug(f'Subtracting {a} - {b} = {result}')
    return result

def mul(a, b):
    result = a * b
    logger.debug(f'Multiplying {a} * {b} = {result}')
    return result

def div(a, b):
    try:
        result = a / b
        logger.debug(f'Dividing {a} / {b} = {result}')
        return result
    except ZeroDivisionError as e:
        logger.error(f"Division by zero error: {e}")
        return None

# Test the functions
add(10, 12)
sub(20, 5)
mul(20, 2)
div(10, 0)  # Intentional error for testing
div(20, 4)
