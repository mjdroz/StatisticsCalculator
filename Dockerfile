FROM python:3.7

ADD . .

CMD [ "python", "./UnitTests/test_calculator.py" ]