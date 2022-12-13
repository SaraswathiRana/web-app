import json

def lambda_handler(event, context):
    content = """
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>Sample Deployment</title>
      <style>
        body {
          color: #ffffff;
          background-color: #0188cc;
          font-family: Arial, sans-serif;
          font-size: 14px;
        }
    
        h1 {
          font-size: 500%;
          font-weight: normal;
          margin-bottom: 0;
        }
    
        h2 {
          font-size: 200%;
          font-weight: normal;
          margin-bottom: 0;
        }
      </style>
    </head>
    <body>
      <div align="center">
        <h1> Congratulations  ...</h1>
        <h2>This application was deployed </h2>
        <p>For next steps, read the <a href="http://aws.amazon.com/documentation/codedeploy">AWS CodeDeploy Documentation</a>.</p>
      </div>
    </body>
    </html>
    """
  
    # TODO implement
    response = {
        'statusCode': 200,
        'body': content,
        "headers": {"Content-Type": "text/html",},
    }
    return response
