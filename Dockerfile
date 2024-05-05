FROM public.ecr.aws/lambda/python:3.8

COPY . .
COPY requirements.txt .
#RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"
RUN pip install -e .
COPY solution/main.py ${LAMBDA_TASK_ROOT}
#WORKDIR /solution

CMD ["main.handler"]