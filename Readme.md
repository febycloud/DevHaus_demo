# Demo Project for DevHaus

## Junior, Intermediate and Expert Developer
Write a program in your language of choice that prints the numbers 1 to 105. But for multiples of three print “Devhaus” instead of the number; for multiples of five print “Learning”; for multiples of seven print “Model”; for multiples of both three and five print “Devhaus Learning”; for multiples of both three and seven print “Devhaus Model”; for multiples of five and seven print the number; for multiples of all of three, five and seven print “Devhaus Learning Model”
Write an automated test that proves that your code works.
Upload the code to GitHub and provide the link prior to your interview.
Prepare a 2-minute maximum presentation on how your code works, where the audience would be another junior developer.
## Intermediate and Expert Developer
1. Create a shell script that would execute your code and sleep for 60 seconds and terminate.
2. From the above, make a multi-stage Dockerfile that compiles your code and executes your test;
the Docker file must have a CMD that executes your shell script.
3. Create a file (can be shell script or GitHub Action) that builds your Docker image.
4. Push the image to a container registry and provide the image link prior to the interview
Prepare a 5-minute maximum presentation on how your code works, where the audience would be a junior developer.
## Expert Developer
Expand the work from above, but instead of sleeping for 60 seconds and terminate, make it run an HTTP server that would work with `curl http://localhost:54321/fizzbuzz` and display the output there as text/plain.
The Dockerfile must have a CMD that runs your server; and must have a HEALTHCHECK.
Automate the build using Github Actions so coverage reports are generated, and images are pushed to a container registry when new code is pushed.
Prepare a 10-minute maximum presentation on how your code works; how the deployment to the registry is implemented and how to manage the changes where the audience would be an intermediate developer.
## This project is based on intermediate Developer

Docker image is here
	···
	docker pull kunosa/demohub:devhaus
	···
