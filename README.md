# Azure Otel Example

## Spring Boot Instrumentation

1. Download the appinsights-agent jar from the [releases](https://github.com/microsoft/ApplicationInsights-Java/releases/tag/3.5.0)
2. Add the jar into your Dockerfile: `COPY applicationinsights-agent-3.5.0.jar applicationinsights-agent.jar`
3. Update Dockerfile entrypoint to include the jar: `ENTRYPOINT ["java", "-javaagent:applicationinsights-agent.jar", "-jar", "app.jar"]`

### Example

```bash
cd spring-boot-backend
mvn clean package
docker build . -t spring-boot:latest
docker run -p 8080:8080 -e APPLICATIONINSIGHTS_CONNECTION_STRING=<Your Connection String> spring-boot:latest
# from here the /time endpoint should return current time. you should see telemetry in app insights
```

## set the env var for app insights
```bash
export APPLICATIONINSIGHTS_CONNECTION_STRING=<Your Connection String>
```

## build and run the image

```bash
docker-compose up --build
```

##