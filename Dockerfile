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

# Define the port your application will run on (if necessary)
EXPOSE 8000

# Command to run the application when the container starts
CMD ["python", "app.py"]
