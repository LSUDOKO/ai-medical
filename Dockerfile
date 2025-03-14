FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY app/ ./app/
COPY static/ ./static/

# Expose the port the app runs on
EXPOSE 7860

# Command to run the application
CMD ["python", "app/gradio_app.py"]