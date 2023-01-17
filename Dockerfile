# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

##### Add environment variables for input and output folders of subtitles and text files
ENV INPUT_FOLDER examples
ENV OUTPUT_FOLDER ss

# mount folders to the container
RUN --mount=type=bind,target=$INPUT_FOLDER 
RUN --mount=type=bind,target=$OUTPUT_FOLDER,rw=true

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app 
USER appuser

##### Run the file with with the folders as arguments and copy output 
CMD ["sh", "-c","python srt2text.py -f $INPUT_FOLDER -d $OUTPUT_FOLDER "]
COPY /$OUTPUT_FOLDER /"$OUTPUT_FOLDER"
