FROM python:3.7

# Set the working directory in the container
WORKDIR /waterfall_model

# Copy the current directory contents into the container
COPY . .

# Install the Python MySQL connector
RUN pip install mysql-connector-python

# Expose the port MySQL typically runs on
EXPOSE 3306

# Run the Python code when the container launches
CMD ["python3", "waterfall.py"]
