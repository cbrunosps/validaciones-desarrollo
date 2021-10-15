"""Show Canary Deployment message."""
import json

# import requests


def lambda_handler(event, context):
    """Muestra el mensaje de un despliegue canario does.

    `PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
        event (dict): API Gateway Lambda Proxy Input Format
        context (obj): Lambda Context runtime methods and attributes

    Returns:
        dict: API Gateway Lambda Proxy Output Format

    .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

    """
    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)
    #     raise e
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "Canary Deployment",
                # "location": ip.text.replace("\n", "")
            }
        ),
    }
