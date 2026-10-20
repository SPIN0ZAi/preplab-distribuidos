FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build

WORKDIR /TodoApi

# Copy everything
COPY . ./

# Restore as distinct layers
RUN dotnet restore

# Build and publish a release
RUN dotnet publish TodoApi.csproj -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:10.0

WORKDIR /TodoApi

COPY --from=build /TodoApi/out .

# Expose the API port
EXPOSE 8080

ENTRYPOINT ["dotnet", "TodoApi.dll"]