# Use official Maven image with Java 17
FROM maven:3.9.2-eclipse-temurin-17 AS build

# Set working directory
WORKDIR /app

# Copy pom.xml and source code
COPY pom.xml .
COPY src ./src

# Build the project
RUN mvn clean package -DskipTests

# Use a smaller Java runtime for final image
FROM eclipse-temurin:17-jre

WORKDIR /app

# Copy built jar from build stage
COPY --from=build /app/target/calculator-1.0-SNAPSHOT.jar ./calculator.jar

# Expose port if needed (optional)
EXPOSE 8080

# Command to run the jar
ENTRYPOINT ["java", "-jar", "calculator.jar"]
