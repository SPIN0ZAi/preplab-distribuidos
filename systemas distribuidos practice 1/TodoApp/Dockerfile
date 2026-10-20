# Download .NET SDK image to container
FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build

# Working directory
WORKDIR /TodoApp

# Copy everything
COPY . ./

# Restore as distinct layers
# can i use only RUN dotnet restore ?
# better solution use WORKDIR TodoApp.Client
RUN dotnet restore TodoApp.Client/TodoApp.Client.csproj

# Build and publish a release
# RUN dotnet publish -o out
RUN dotnet publish TodoApp.Client/TodoApp.Client.csproj -c Release -o TodoApp.Client/out

# Final stage: use Nginx to serve static files
FROM nginx:alpine AS final
WORKDIR /usr/share/nginx/html

# Copy wwwroot and nginx configuration. Do not touch, please these two lines
# . is the current directory in the container, which is /usr/share/nginx/html
COPY --from=build /TodoApp/TodoApp.Client/out/wwwroot . 
# this is the nginx configuration file, which is located in the nginx folder in the root of the project
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80