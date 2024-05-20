# sprayfoam
Tiny docker image which creates tons of large files. Created for testing args provided to deployments on kthcloud.

## Usage
- Run the image as a deployment on kthcloud with an attached volume
- Two environment variables are available
  - `VOLUME` - the path to the volume to write files to
  - `SIZE` - the size of the files to create in MB
