import decimal

def lambda_handler(event, context):

    speed = event["speed"]
    real = event["real"]
    return calc(speed, real)

def calc(speed, real):
    return speed * real * decimal.Decimal(0.1234)
