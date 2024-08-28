  UW PICO 5.09                    File: Dockerfile                    Modified  

# Base image with Python 3.8
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]


^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  
