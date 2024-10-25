FROM mcr.microsoft.com/openjdk/jdk:17-mariner
WORKDIR /app
COPY target/*.jar app.jar
COPY applicationinsights-agent-3.5.0.jar applicationinsights-agent.jar
ENTRYPOINT ["java", "-javaagent:applicationinsights-agent.jar", "-jar", "app.jar"]