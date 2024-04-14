FROM public.ecr.aws/lambda/python:3.12

LABEL maintainer=Clooooode<clode@clo5de.info>

# Copy requirements.txt
COPY requirements-lambda.txt ${LAMBDA_TASK_ROOT}

# Copy function code
COPY manager ${LAMBDA_TASK_ROOT}/manager
COPY stage ${LAMBDA_TASK_ROOT}/stage
COPY utils ${LAMBDA_TASK_ROOT}/utils
COPY lambda_app.py ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN pip install -r requirements-lambda.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "lambda_app.stage_info_handler" ]