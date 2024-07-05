# Use the official Python LTS image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the files needed to install dependencies
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the files
COPY . .


# Create a simple hello.txt file
RUN echo "Hello, world!" > hello.txt

RUN python -u digit_classification.py

ENTRYPOINT ["python", "-u", "digit_classification.py"]


