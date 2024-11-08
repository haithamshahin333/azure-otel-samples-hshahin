FROM mcr.microsoft.com/openjdk/jdk:17-mariner
WORKDIR /app
COPY target/*.jar app.jar
COPY applicationinsights-agent-3.6.2.jar applicationinsights-agent-3.6.2.jar
COPY applicationinsights.json applicationinsights.json
ENTRYPOINT ["java", "-javaagent:applicationinsights-agent-3.6.2.jar", "-jar", "app.jar"]
