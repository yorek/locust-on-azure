# https://docs.locust.io/en/stable/running-locust-docker.html#running-locust-with-docker
docker run -p 8089:8089 -v c:/dockershare:/mnt/locust locustio/locust:1.0.3 -f /mnt/locust/locustfile.py