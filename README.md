# Azure Otel Example

## Java Instrumentation (Example here using Spring Boot)

1. Download the appinsights-agent jar from the [releases](https://github.com/microsoft/ApplicationInsights-Java/releases/download/3.6.2/applicationinsights-agent-3.6.2.jar)
2. Add the jar into your Dockerfile: `COPY applicationinsights-agent-3.6.2.jar applicationinsights-agent-3.6.2.jar`
3. Update your config file (the agent is looking for the name `applicationinsights.json` in the same directory as the jar) and add in your Dockerfile to the same directory as the command above: `COPY applicationinsights.json applicationinsights.json`. Be sure to include relevant configs according to the scheme: https://learn.microsoft.com/en-us/azure/azure-monitor/app/java-standalone-config
4. Update Dockerfile entrypoint to include the jar: `ENTRYPOINT ["java", "-javaagent:applicationinsights-agent-3.6.2.jar", "-jar", "app.jar"]`

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
